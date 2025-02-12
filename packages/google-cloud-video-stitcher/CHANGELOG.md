# Changelog

## [0.7.5](https://github.com/googleapis/google-cloud-python/compare/google-cloud-video-stitcher-v0.7.4...google-cloud-video-stitcher-v0.7.5) (2023-12-07)


### Features

* Add support for python 3.12 ([31d043d](https://github.com/googleapis/google-cloud-python/commit/31d043de5a0b8bd329e8d5a36e7811d5ea7bd7a1))
* Introduce compatibility with native namespace packages ([31d043d](https://github.com/googleapis/google-cloud-python/commit/31d043de5a0b8bd329e8d5a36e7811d5ea7bd7a1))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([31d043d](https://github.com/googleapis/google-cloud-python/commit/31d043de5a0b8bd329e8d5a36e7811d5ea7bd7a1))
* Use `retry_async` instead of `retry` in async client ([31d043d](https://github.com/googleapis/google-cloud-python/commit/31d043de5a0b8bd329e8d5a36e7811d5ea7bd7a1))

## [0.7.4](https://github.com/googleapis/python-video-stitcher/compare/v0.7.3...v0.7.4) (2023-09-19)


### ⚠ BREAKING CHANGES

* use correct child_type annotation

### Bug Fixes

* Use correct child_type annotation ([bd0af89](https://github.com/googleapis/python-video-stitcher/commit/bd0af892653db462b0c2b3389faf03ebe0d4d49c))


### Documentation

* Minor formatting ([88e37ed](https://github.com/googleapis/python-video-stitcher/commit/88e37edab40affdd8a9e9dfe83d24a615a422643))
* Remove migrated samples ([#180](https://github.com/googleapis/python-video-stitcher/issues/180)) ([73af7e9](https://github.com/googleapis/python-video-stitcher/commit/73af7e90d9f71aa322cb940b3b1c1e995aa72484))

## [0.7.3](https://github.com/googleapis/python-video-stitcher/compare/v0.7.2...v0.7.3) (2023-07-04)


### Bug Fixes

* Add async context manager return types ([#161](https://github.com/googleapis/python-video-stitcher/issues/161)) ([c97054a](https://github.com/googleapis/python-video-stitcher/commit/c97054a6f226b48c7e9b1d70bbf466a590ababdd))

## [0.7.2](https://github.com/googleapis/python-video-stitcher/compare/v0.7.1...v0.7.2) (2023-05-25)


### Documentation

* **samples:** Add samples for live config and live session ([b2f73e7](https://github.com/googleapis/python-video-stitcher/commit/b2f73e76e5f88287903d50db9478e07bfefcaf39))
* **samples:** Update slates and CDN keys to use LROs ([b2f73e7](https://github.com/googleapis/python-video-stitcher/commit/b2f73e76e5f88287903d50db9478e07bfefcaf39))

## [0.7.1](https://github.com/googleapis/python-video-stitcher/compare/v0.7.0...v0.7.1) (2023-05-15)


### Bug Fixes

* Remove default_ad_break_duration from LiveConfig  ([08c1a06](https://github.com/googleapis/python-video-stitcher/commit/08c1a068ff4127f2ff929700e5254c61d8ca8f83))
* Remove GamVodConfig ([08c1a06](https://github.com/googleapis/python-video-stitcher/commit/08c1a068ff4127f2ff929700e5254c61d8ca8f83))

## [0.7.0](https://github.com/googleapis/python-video-stitcher/compare/v0.6.1...v0.7.0) (2023-03-27)


### Features

* LiveSession changes for live config ([93971ed](https://github.com/googleapis/python-video-stitcher/commit/93971ed42dd850c4f432decb44a1814163815b30))
* LRO changes for CdnKey and Slate methods ([93971ed](https://github.com/googleapis/python-video-stitcher/commit/93971ed42dd850c4f432decb44a1814163815b30))
* VodSession changes for ad tracking ([93971ed](https://github.com/googleapis/python-video-stitcher/commit/93971ed42dd850c4f432decb44a1814163815b30))


### Bug Fixes

* Add AdTracking as a required parameter for VodSession ([93971ed](https://github.com/googleapis/python-video-stitcher/commit/93971ed42dd850c4f432decb44a1814163815b30))

## [0.6.1](https://github.com/googleapis/python-video-stitcher/compare/v0.6.0...v0.6.1) (2023-01-23)


### Bug Fixes

* Add context manager return types ([6bc0894](https://github.com/googleapis/python-video-stitcher/commit/6bc0894934e1038bca35f4af70279b0f49471b09))


### Documentation

* Add documentation for enums ([6bc0894](https://github.com/googleapis/python-video-stitcher/commit/6bc0894934e1038bca35f4af70279b0f49471b09))

## [0.6.0](https://github.com/googleapis/python-video-stitcher/compare/v0.5.1...v0.6.0) (2023-01-12)


### Features

* Add support for python 3.11 ([#117](https://github.com/googleapis/python-video-stitcher/issues/117)) ([5885372](https://github.com/googleapis/python-video-stitcher/commit/58853726906c8a4987f4c6bfe045480021766628))

## [0.5.1](https://github.com/googleapis/python-video-stitcher/compare/v0.5.0...v0.5.1) (2023-01-05)


### Documentation

* **samples:** Add Media CDN samples ([b905053](https://github.com/googleapis/python-video-stitcher/commit/b9050531174536744f967548829f4325ab4d53e3))
* **samples:** Move Akamai sample to its own file ([b905053](https://github.com/googleapis/python-video-stitcher/commit/b9050531174536744f967548829f4325ab4d53e3))

## [0.5.0](https://github.com/googleapis/python-video-stitcher/compare/v0.4.0...v0.5.0) (2022-12-15)


### Features

* Add support for `google.cloud.video.stitcher.__version__` ([b45d82a](https://github.com/googleapis/python-video-stitcher/commit/b45d82a9836eb96cf7c21475887897e1a1eb9c93))
* Add typing to proto.Message based class attributes ([b45d82a](https://github.com/googleapis/python-video-stitcher/commit/b45d82a9836eb96cf7c21475887897e1a1eb9c93))


### Bug Fixes

* Add dict typing for client_options ([b45d82a](https://github.com/googleapis/python-video-stitcher/commit/b45d82a9836eb96cf7c21475887897e1a1eb9c93))
* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0  ([25011aa](https://github.com/googleapis/python-video-stitcher/commit/25011aadee2f8018c078b9dc2df483393efcab2b))
* Drop usage of pkg_resources ([25011aa](https://github.com/googleapis/python-video-stitcher/commit/25011aadee2f8018c078b9dc2df483393efcab2b))
* Fix timeout default values ([25011aa](https://github.com/googleapis/python-video-stitcher/commit/25011aadee2f8018c078b9dc2df483393efcab2b))


### Documentation

* **samples:** Snippetgen handling of repeated enum field ([b45d82a](https://github.com/googleapis/python-video-stitcher/commit/b45d82a9836eb96cf7c21475887897e1a1eb9c93))
* **samples:** Snippetgen should call await on the operation coroutine before calling result ([25011aa](https://github.com/googleapis/python-video-stitcher/commit/25011aadee2f8018c078b9dc2df483393efcab2b))

## [0.4.0](https://github.com/googleapis/python-video-stitcher/compare/v0.3.2...v0.4.0) (2022-10-27)


### Features

* Add support for Media CDN ([#98](https://github.com/googleapis/python-video-stitcher/issues/98)) ([df58bb7](https://github.com/googleapis/python-video-stitcher/commit/df58bb77d5109c0d08c10cbc0a4d0f3ebd7c2c69))

## [0.3.2](https://github.com/googleapis/python-video-stitcher/compare/v0.3.1...v0.3.2) (2022-10-10)


### Bug Fixes

* **deps:** allow protobuf 3.19.5 ([61653d5](https://github.com/googleapis/python-video-stitcher/commit/61653d5627762a886718478a232053841a63b947))
* **deps:** require google-api-core&gt;=1.33.2 ([61653d5](https://github.com/googleapis/python-video-stitcher/commit/61653d5627762a886718478a232053841a63b947))

## [0.3.1](https://github.com/googleapis/python-video-stitcher/compare/v0.3.0...v0.3.1) (2022-10-03)


### Bug Fixes

* **deps:** Require protobuf >= 3.20.2 ([#84](https://github.com/googleapis/python-video-stitcher/issues/84)) ([825e000](https://github.com/googleapis/python-video-stitcher/commit/825e000049ad910395b7218f117a00ed6300a62f))


### Documentation

* **samples:** Fix Video Stitcher region tag prefix ([#86](https://github.com/googleapis/python-video-stitcher/issues/86)) ([5b70a6b](https://github.com/googleapis/python-video-stitcher/commit/5b70a6bb5e9f54fd8535a3cd6d18ecbafeb2ec5d))
* Update github repo url ([#88](https://github.com/googleapis/python-video-stitcher/issues/88)) ([07adb7b](https://github.com/googleapis/python-video-stitcher/commit/07adb7bbea3905760c3e46c4200598c8e9cef50b))

## [0.3.0](https://github.com/googleapis/python-video-stitcher/compare/v0.2.1...v0.3.0) (2022-09-16)


### Features

* Add support for REST transport ([#75](https://github.com/googleapis/python-video-stitcher/issues/75)) ([48e8350](https://github.com/googleapis/python-video-stitcher/commit/48e8350b931f39aa3484cfa935b4ca75f9c0d04e))


### Bug Fixes

* **deps:** require google-api-core>=1.33.1,>=2.8.0 ([48e8350](https://github.com/googleapis/python-video-stitcher/commit/48e8350b931f39aa3484cfa935b4ca75f9c0d04e))
* **deps:** require protobuf >= 3.20.1 ([48e8350](https://github.com/googleapis/python-video-stitcher/commit/48e8350b931f39aa3484cfa935b4ca75f9c0d04e))

## [0.2.1](https://github.com/googleapis/python-video-stitcher/compare/v0.2.0...v0.2.1) (2022-08-11)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#53](https://github.com/googleapis/python-video-stitcher/issues/53)) ([42d07be](https://github.com/googleapis/python-video-stitcher/commit/42d07be69e0dd60f55de4619645c0d14c47f8660))
* **deps:** require proto-plus >= 1.22.0 ([42d07be](https://github.com/googleapis/python-video-stitcher/commit/42d07be69e0dd60f55de4619645c0d14c47f8660))

## [0.2.0](https://github.com/googleapis/python-video-stitcher/compare/v0.1.2...v0.2.0) (2022-07-16)


### Features

* add asset_id and stream_id fields to VodSession and LiveSession responses ([fefdc9c](https://github.com/googleapis/python-video-stitcher/commit/fefdc9c581eb59e227598780ab7dd5752cf9c1f0))
* add audience parameter ([fefdc9c](https://github.com/googleapis/python-video-stitcher/commit/fefdc9c581eb59e227598780ab7dd5752cf9c1f0))


### Bug Fixes

* **deps:** require google-api-core>=1.32.0,>=2.8.0 ([#45](https://github.com/googleapis/python-video-stitcher/issues/45)) ([a5ec756](https://github.com/googleapis/python-video-stitcher/commit/a5ec756544d37bb461fb947d6dc8b6aad966a481))
* remove COMPLETE_POD stitching option ([fefdc9c](https://github.com/googleapis/python-video-stitcher/commit/fefdc9c581eb59e227598780ab7dd5752cf9c1f0))
* require python 3.7+ ([#43](https://github.com/googleapis/python-video-stitcher/issues/43)) ([5c952d8](https://github.com/googleapis/python-video-stitcher/commit/5c952d8eb36f5d8a20526e44f8a38e46debe8962))

## [0.1.2](https://github.com/googleapis/python-video-stitcher/compare/v0.1.1...v0.1.2) (2022-06-03)


### Bug Fixes

* **deps:** require protobuf <4.0.0dev ([#34](https://github.com/googleapis/python-video-stitcher/issues/34)) ([109ca6e](https://github.com/googleapis/python-video-stitcher/commit/109ca6e723b951c8f474beec236dfed8ac0929dc))


### Documentation

* fix changelog header to consistent size ([#35](https://github.com/googleapis/python-video-stitcher/issues/35)) ([286c3a0](https://github.com/googleapis/python-video-stitcher/commit/286c3a0be0c4aef079ee7fe57634982a9621711f))
* **samples:** add code samples ([#17](https://github.com/googleapis/python-video-stitcher/issues/17)) ([ed60215](https://github.com/googleapis/python-video-stitcher/commit/ed60215424f1ea0015c44033cea931d9a80c9539))

## [0.1.1](https://github.com/googleapis/python-video-stitcher/compare/v0.1.0...v0.1.1) (2022-03-05)


### Bug Fixes

* **deps:** require google-api-core>=1.31.5, >=2.3.2 ([#10](https://github.com/googleapis/python-video-stitcher/issues/10)) ([5451292](https://github.com/googleapis/python-video-stitcher/commit/5451292d68416c0246419f31909cf50c1d5b10de))

## 0.1.0 (2022-02-23)


### Features

* add v1 ([f164d04](https://github.com/googleapis/python-video-stitcher/commit/f164d04468c38a635d76626cdbf502d37fde4d8c))
