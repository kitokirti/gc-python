#  Copyright 2022 Google LLC
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
# flake8: noqa


# This file is automatically generated. Please do not modify it directly.
# Find the relevant recipe file in the samples/recipes or samples/ingredients
# directory and apply your changes there.


# [START compute_custom_machine_type_update_memory]
import time

from google.cloud import compute_v1


def add_extended_memory_to_instance(
    project_id: str, zone: str, instance_name: str, new_memory: int
):
    """
    Modify an existing VM to use extended memory.

    Args:
        project_id: project ID or project number of the Cloud project you want to use.
        zone: name of the zone to create the instance in. For example: "us-west3-b"
        instance_name: name of the new virtual machine (VM) instance.
        new_memory: the amount of memory for the VM instance, in megabytes.

    Returns:
        Instance object.
    """
    instance_client = compute_v1.InstancesClient()
    operation_client = compute_v1.ZoneOperationsClient()
    instance = instance_client.get(
        project=project_id, zone=zone, instance=instance_name
    )

    if not (
        "n1-" in instance.machine_type
        or "n2-" in instance.machine_type
        or "n2d-" in instance.machine_type
    ):
        raise RuntimeError("Extra memory is available only for N1, N2 and N2D CPUs.")

    # Make sure that the machine is turned off
    if instance.status not in (
        instance.Status.TERMINATED.name,
        instance.Status.STOPPED.name,
    ):
        op = instance_client.stop_unary(
            project=project_id, zone=zone, instance=instance_name
        )
        operation_client.wait(project=project_id, zone=zone, operation=op.name)
        start = time.time()
        while instance.status not in (
            instance.Status.TERMINATED.name,
            instance.Status.STOPPED.name,
        ):
            # Waiting for the instance to be turned off.
            instance = instance_client.get(
                project=project_id, zone=zone, instance=instance_name
            )
            time.sleep(2)
            if time.time() - start >= 300:  # 5 minutes
                raise TimeoutError()

    # Modify the machine definition, remember that extended memory is available only for N1, N2 and N2D CPUs
    start, end = instance.machine_type.rsplit("-", maxsplit=1)
    instance.machine_type = start + f"-{new_memory}-ext"
    # TODO: If you prefer to use the CustomMachineType helper class, uncomment this code and comment the 2 lines above
    # Using CustomMachineType helper
    # cmt = CustomMachineType.from_str(instance.machine_type)
    # cmt.memory_mb = new_memory
    # cmt.extra_memory_used = True
    # instance.machine_type = str(cmt)
    op = instance_client.update_unary(
        project=project_id,
        zone=zone,
        instance=instance_name,
        instance_resource=instance,
    )
    operation_client.wait(project=project_id, zone=zone, operation=op.name)

    return instance_client.get(project=project_id, zone=zone, instance=instance_name)


# [END compute_custom_machine_type_update_memory]
