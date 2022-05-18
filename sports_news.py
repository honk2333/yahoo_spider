import requests
import json
import time

cookies = {
    'A1': 'd=AQABBKdthGICEK8hBlDgI5CT3Y34fV-twi4FEgEBAQG_hWKOYgAAAAAA_eMAAA&S=AQAAAlMbDCLi9tFu0fR38Z_nXHE',
    'A3': 'd=AQABBKdthGICEK8hBlDgI5CT3Y34fV-twi4FEgEBAQG_hWKOYgAAAAAA_eMAAA&S=AQAAAlMbDCLi9tFu0fR38Z_nXHE',
    'A1S': 'd=AQABBKdthGICEK8hBlDgI5CT3Y34fV-twi4FEgEBAQG_hWKOYgAAAAAA_eMAAA&S=AQAAAlMbDCLi9tFu0fR38Z_nXHE&j=WORLD',
    'GUC': 'AQEBAQFihb9ijkIhKQSZ',
    'cmp': 't=1652853195&j=0&u=1---',
    'thamba': '2',
    'maex': '%7B%22993a4214%22%3A1652855423%2C%22eafaf0a6%22%3A1652855423%7D',
    '_dd_s': 'logs=1&id=419e46b8-4d27-41b1-934d-c9e8ebb80575&created=1652855317476&expire=1652856326769',
}

headers = {
    'authority': 'sports.yahoo.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    # Already added when you pass json=
    'content-type': 'application/json',
    # Requests sorts cookies= alphabetically
    'cookie': 'A1=d=AQABBKdthGICEK8hBlDgI5CT3Y34fV-twi4FEgEBAQG_hWKOYgAAAAAA_eMAAA&S=AQAAAlMbDCLi9tFu0fR38Z_nXHE; A3=d=AQABBKdthGICEK8hBlDgI5CT3Y34fV-twi4FEgEBAQG_hWKOYgAAAAAA_eMAAA&S=AQAAAlMbDCLi9tFu0fR38Z_nXHE; A1S=d=AQABBKdthGICEK8hBlDgI5CT3Y34fV-twi4FEgEBAQG_hWKOYgAAAAAA_eMAAA&S=AQAAAlMbDCLi9tFu0fR38Z_nXHE&j=WORLD; GUC=AQEBAQFihb9ijkIhKQSZ; cmp=t=1652853195&j=0&u=1---; thamba=2; maex=%7B%22993a4214%22%3A1652855423%2C%22eafaf0a6%22%3A1652855423%7D; _dd_s=logs=1&id=419e46b8-4d27-41b1-934d-c9e8ebb80575&created=1652855317476&expire=1652856326769',
    'origin': 'https://sports.yahoo.com',
    'referer': 'https://sports.yahoo.com/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'x-webp': '1',
}

params = {
    'bkt': 'sp_mab_personalized_odds_cntrl,JARVISSPORTSDESKSPEOL04',
    'crumb': 'L/yDE8AF9QD',
    'device': 'desktop',
    'ecma': 'modern',
    'feature': 'article2_csn,canvassOffnet,enableCMP,enableConsentData,enableYBarFavTeams,sp-nav-test,oathPlayer,enableCCPAFooter,enableReconsent,showFutures,enableUserService,disableCommentsMessage,enableLGPD,watchtogether,enableXrayNcp,enableXrayPeopleSportsEntities,enableXrayTeamEntities,enableXrayTopicEntities,enableAdlite,enableAdLiteUpSellFeedback,enableLeagueDraftOdds,enableLeagueFutures,enableLeagueProps,enableMonalixa3pBodySlot,enableMonalixaBodySlot,enableMonalixaPlacements,enableMonalixaYBarUpsell,enableXrayAthleteHeaderV2,enableXrayNcpV2SalienceMerge,livecoverage,newContentAttribution,caasSmartphone,canvass,desktopNotifications,searchAssist,licensed-only,dfsFavoriteTeamPromo,enableOlyAthletePage,enableGameDriveOdds,yahooDayOne,playerNews,enableMonalixaNcaabBanner,newLogo,sponsoredAds',
    'intl': 'us',
    'lang': 'en-US',
    'partner': 'none',
    'prid': '750068ph894ju',
    'region': 'US',
    'site': 'sports',
    'tz': 'Asia/Japan',
    'ver': '1.0.9127',
}

json_data = {
    'requests': {
        'g0': {
            'resource': 'SportsStreamService',
            'operation': 'read',
            'params': {
                'ui': {
                    'comments_offnet': True,
                    'editorial_featured_count': 1,
                    'image_quality_override': True,
                    'link_out_allowed': True,
                    'needtoknow_template': 'carousel',
                    'ntk_bypassA3c': True,
                    'pubtime_maxage': 21600,
                    'relative_links': True,
                    'smart_crop': True,
                    'storyline_count': 2,
                    'storyline_enabled': True,
                    'storyline_min': 2,
                    'summary': True,
                    'thumbnail_size': 100,
                    'view': 'mega',
                    'editorial_content_count': 19,
                    'editorial_content_min': 4,
                    'finance_upsell_threshold': 4,
                    'isDesktopCarousel': True,
                    'roundup': True,
                    'sports_morelink_enabled': True,
                },
                'additional_subsite': 'sportsreel',
                'category': 'YCT:001000001',
                'forceJpg': True,
                'releasesParams': {
                    'limit': 20,
                    'offset': 0,
                },
                'ncpParams': {
                    'query': {
                        'mabEnabled': True,
                        'mabContentEnabled': True,
                        'version': 'v2',
                        'configId': '',
                        'namespace': 'sports',
                    },
                    'body': {
                        'gqlVariables': {
                            'main': {
                                'pagination': {
                                    'uuids': 'paginationString={"streamPagination":{"uuids":[{"id":"915c7017-b729-3211-977e-1975da216137","type":"ymedia:type=story"},{"id":"a4a302eb-a737-3c11-92bc-900322197258","type":"ymedia:type=story"},{"id":"33a7eff5-a67c-38b8-afdc-71aa47d2ed28","type":"ymedia:type=story"},{"id":"571a3486-0339-3b63-86c7-fca6b4d5d921","type":"ymedia:type=story"},{"id":"ff75d280-f430-37ba-90b4-bbed547c9557","type":"ymedia:type=story"},{"id":"973d7aac-0459-33b2-b4fe-1ce4481d5199","type":"ymedia:type=story"},{"id":"7fc42378-7e28-3073-abce-ffdbefec150c","type":"ymedia:type=story"},{"id":"ecbf1411-1576-390b-a0f2-8c797a80ca3f","type":"ymedia:type=story"},{"id":"56563499-4654-3acd-b920-682e5e8b6615","type":"ymedia:type=story"},{"id":"93ccad7a-8d0c-338d-9b85-40f3b82927b9","type":"ymedia:type=story"},{"id":"1b513a69-07a3-3e52-86d9-b777de4087a8","type":"ymedia:type=story"},{"id":"edd37bd0-5ad3-3ab5-897d-47accd630363","type":"ymedia:type=story"},{"id":"7fa51d15-1c87-3560-a2e3-d5c7a3ce03c7","type":"ymedia:type=story"},{"id":"20a541da-9c87-3542-8f4e-7867c4396689","type":"ymedia:type=story"},{"id":"52903df5-cb25-311f-a231-d055f78b9da1","type":"ymedia:type=story"},{"id":"ffc97734-94d1-4bf3-ae4d-31f08c9fdd40","type":"ymedia:type=story"},{"id":"b3855d7d-c16f-30b7-9194-7f34c005e5ea","type":"ymedia:type=story"},{"id":"a03b51e6-16ff-3172-bb76-206ebc0156ba","type":"ymedia:type=story"},{"id":"48cf1c33-6cd8-37fe-bfb8-6c31820aba2d","type":"ymedia:type=story"},{"id":"cfafb247-e436-3e46-81c6-f4168fca4007","type":"ymedia:type=story"},{"id":"15fe9805-3ae6-34ea-b047-2e2f268a7461","type":"ymedia:type=story"},{"id":"ecf349af-5c37-3373-a7c4-c5579c4ce401","type":"ymedia:type=story"},{"id":"cdbc3c48-a0da-3e9d-9d95-f0d169305857","type":"ymedia:type=story"},{"id":"681b10e9-0789-3855-a561-c7eca108351b","type":"ymedia:type=story"},{"id":"0aaafc02-589a-3907-bd56-c45a24fbe1a2","type":"ymedia:type=story"},{"id":"b2880e91-8fb6-3da3-82e8-1e687d84741e","type":"ymedia:type=story"},{"id":"e6b1868f-5426-3aa1-9f1a-6c45bf6d614f","type":"ymedia:type=story"},{"id":"2870d55b-1860-3bc1-a537-c723aa978cd9","type":"ymedia:type=story"},{"id":"dc5724a4-1284-3d0c-980d-03b4de98ef91","type":"ymedia:type=story"},{"id":"2def162f-e0e8-32ff-b089-b49c20a0112a","type":"ymedia:type=story"},{"id":"7e98946c-fb15-3338-bee3-76046732b678","type":"ymedia:type=cavideo"},{"id":"0feb5325-3e76-377a-a552-b1cb45164025","type":"ymedia:type=story"},{"id":"c67b0b83-d4b3-3122-bd9a-c44b0ee5cf22","type":"ymedia:type=story"},{"id":"aae3a5bc-fdaf-3f3b-b357-6349753760d2","type":"ymedia:type=story"},{"id":"4ba70471-c682-3c04-9639-b13d9c910aa5","type":"ymedia:type=story"},{"id":"93a95f29-757f-362b-a6af-61fc0bd76e1c","type":"ymedia:type=story"},{"id":"a1836559-029c-368b-be89-92960f54936b","type":"ymedia:type=story"},{"id":"2b8180c5-f146-39b7-a183-9e1f83ee5078","type":"ymedia:type=story"},{"id":"766783f0-420b-3366-9664-262014556e8e","type":"ymedia:type=story"},{"id":"9c333b76-ec9f-3965-97ff-c9f66a213ecd","type":"ymedia:type=story"},{"id":"5db81708-1a96-3a4e-8618-666dbb7b6fe0","type":"ymedia:type=story"},{"id":"6321c7db-59c7-30ae-8c71-021c539a0c49","type":"ymedia:type=story"},{"id":"a44d6406-b289-36ca-9f0d-0357811121a2","type":"ymedia:type=cavideo"},{"id":"0c95ca5d-db04-30f2-b1e9-0f60a7d2c687","type":"ymedia:type=story"},{"id":"6c961852-6a53-3dc9-be38-624570afe3ed","type":"ymedia:type=story"},{"id":"04a6e079-8974-34d1-8c24-604de4e7a092","type":"ymedia:type=story"},{"id":"478bf55b-ed9e-4ef2-9a04-ce51e3c5adf5","type":"ymedia:type=story"},{"id":"8df8d176-e0f2-3e4c-909f-74706c699817","type":"ymedia:type=story"},{"id":"62dea45a-1407-3829-91b1-7bbd43e4bf83","type":"ymedia:type=story"},{"id":"d1491c0d-eed4-335e-8e30-98df1e4b5a9e","type":"ymedia:type=story"},{"id":"775076fd-78a5-3932-83d2-7bb14b841a97","type":"ymedia:type=story"},{"id":"1d75a957-81b9-33b9-a75b-862eb20b76ed","type":"ymedia:type=story"},{"id":"0d279a07-2b55-3cef-9a81-6cae8b4e66ea","type":"ymedia:type=story"},{"id":"4cbd1fbe-f5ac-31db-a62e-ac33c61e1048","type":"ymedia:type=story"},{"id":"36140ae3-68e7-3c30-b9f5-6bfc5a927e43","type":"ymedia:type=story"},{"id":"2bd82c0c-ff24-3ff4-b313-48ca30f928ba","type":"ymedia:type=story"},{"id":"ded4a799-9c6d-33ad-a9f9-c694add6c3cb","type":"ymedia:type=story"},{"id":"40b4208b-60a5-4ff6-b257-235718e7410a","type":"ymedia:type=story"},{"id":"6b040bf8-7078-4096-a6f4-b64c98943a3f","type":"ymedia:type=story"},{"id":"a7e4477f-41ec-3467-a021-2ba3829d05d3","type":"ymedia:type=story"},{"id":"397210e8-c114-356b-ac31-5c4a5e15998c","type":"ymedia:type=story"},{"id":"4f7e73b5-592c-3f24-834b-bcea3981ade9","type":"ymedia:type=story"},{"id":"f0c90f94-0ec8-3113-8e72-6c1e1a7e0525","type":"ymedia:type=story"},{"id":"bea12b79-9aa5-3662-913c-b224fe2ba270","type":"ymedia:type=story"},{"id":"afca2a11-edd6-3195-aa90-d91eae50467d","type":"ymedia:type=story"},{"id":"ee1c7176-1584-38cd-9027-198ecf72a5e0","type":"ymedia:type=story"},{"id":"681b6185-4574-339a-9376-07e08590c1f4","type":"ymedia:type=story"},{"id":"ee123b93-2e3e-34d9-8f47-eed8ae9978b5","type":"ymedia:type=story"},{"id":"ec4ebc5f-771e-33cb-bfb2-bd72d89ee41a","type":"ymedia:type=story"},{"id":"297ccc32-c84c-4ca5-8a90-cd5540127aa7","type":"ymedia:type=story"},{"id":"3cdd651f-b815-3c91-87f6-54b1189fc275","type":"ymedia:type=story"},{"id":"d2d55e9e-ab20-3b54-b596-6f8e3c776247","type":"ymedia:type=story"},{"id":"06094a35-c944-3906-892e-25851fe30119","type":"ymedia:type=story"},{"id":"51a30db4-8afb-30de-b3f8-27a0b6cd10bd","type":"ymedia:type=story"},{"id":"ba08f91e-22e3-3f19-8320-04b3e646ccca","type":"ymedia:type=cavideo"},{"id":"6f7a1dab-b055-3bb7-8fb6-439b76d8decd","type":"ymedia:type=story"},{"id":"cf4c5cd0-03ee-3b96-b521-c6a1c5f1f67a","type":"ymedia:type=story"},{"id":"941ba0d1-7a0c-3a38-af16-02bc7df7611f","type":"ymedia:type=story"},{"id":"012e4a00-1ac0-383d-940c-13f3e5fe79ff","type":"ymedia:type=story"},{"id":"894c5caf-4f4f-3b29-aa4d-5367e9c0b5f6","type":"ymedia:type=story"},{"id":"22a38b9f-444c-330b-b1e5-2e14b7e6016d","type":"ymedia:type=story"},{"id":"d46cab99-e3ed-3039-b8c3-7eca60a17fc5","type":"ymedia:type=story"},{"id":"b864d959-19a7-3430-977f-ba3d59498c4e","type":"ymedia:type=story"},{"id":"5ecec529-3282-3a72-a6fb-ebe13c0ca664","type":"ymedia:type=story"},{"id":"604e8fbb-208c-3ced-a21e-88e94c298fda","type":"ymedia:type=story"},{"id":"6b22288e-80c5-303a-9cf1-6499799b5b57","type":"ymedia:type=story"},{"id":"bb51f2d6-d966-38e9-9c0a-42c5a1ca09b0","type":"ymedia:type=story"},{"id":"697871e6-89aa-389c-ab9a-4a3decf13543","type":"ymedia:type=story"},{"id":"f3759bd3-1926-3891-bbe7-88179124a4bc","type":"ymedia:type=story"},{"id":"70b01d31-67cf-3750-9e38-7462ad792472","type":"ymedia:type=story"},{"id":"d9086187-616e-318d-9b89-5ad9915cb7bc","type":"ymedia:type=story"},{"id":"e311cfc7-dfcf-3b35-bf0f-b6f84f333c54","type":"ymedia:type=story"},{"id":"ab01a0b1-40ed-3275-aba8-2e4948018de7","type":"ymedia:type=story"},{"id":"0d6fde8c-f1eb-3a34-a3c4-1fffa1a4572a","type":"ymedia:type=story"},{"id":"418edc7b-75e1-362a-b5d5-b1dfda05930b","type":"ymedia:type=story"},{"id":"786d5e5a-230a-4ec8-a193-dd8d5f4641ba","type":"ymedia:type=story"},{"id":"a841f07c-92b6-375b-a44d-e438fc785b40","type":"ymedia:type=story"},{"id":"5db16e4f-7ac9-3e6a-a276-9b00bd67fcb3","type":"ymedia:type=story"},{"id":"8b5828a8-ee36-3758-ae43-0d4049528d43","type":"ymedia:type=story"},{"id":"c5bcbadb-18c4-3bb3-b8d1-07309e0ff569","type":"ymedia:type=story"},{"id":"c8f96140-6801-328b-ad40-e61c1748fd86","type":"ymedia:type=story"},{"id":"25d1e054-bb65-3a0f-897f-be2694e83e17","type":"ymedia:type=story"},{"id":"77beb89e-cce9-3381-984e-570350886f1f","type":"ymedia:type=story"},{"id":"e6bc6964-6050-3ab5-a7c5-9ec36e3dce47","type":"ymedia:type=story"},{"id":"3e30e2c6-49f0-33c6-b370-4b49af6f278c","type":"ymedia:type=story"},{"id":"fba14df8-7e7a-33a6-8e4b-c903f10a2ce6","type":"ymedia:type=story"},{"id":"94b0d2e7-d361-34c7-98f7-c58498c5efae","type":"ymedia:type=story"},{"id":"d885ad47-8c8e-3ffe-9258-a6a88535532f","type":"ymedia:type=story"},{"id":"73927348-437a-399e-a19b-4afd3b438e88","type":"ymedia:type=story"},{"id":"7ad55dfc-42dc-381d-80c0-0db08dc5ad34","type":"ymedia:type=story"}],"seenHits":[{"id":"7588270a-9a99-3d42-99ed-8bb7d2ace717","type":"ymedia:type=story"},{"id":"15fe4945-67d3-3d4a-98b8-33c336094f3d","type":"ymedia:type=story","storyline":[{"id":"3342e57a-f2cc-4ff6-a6bf-f0ac22f8b7ed","type":"ymedia:type=story"},{"id":"337c2f49-98a8-3fa8-9c41-c361b8b032d7","type":"ymedia:type=cavideo"}]},{"id":"219be70b-7e45-4a50-9fd2-e135f97d77f1","type":"ymedia:type=story","storyline":[{"id":"da142f56-fb12-33e3-a8cf-b59efddb6d62","type":"ymedia:type=story"},{"id":"45d17209-ae69-322c-83e7-96023b97b394","type":"ymedia:type=story"}]},{"id":"4757a78f-0474-330a-bdda-65b0d737b1e2","type":"ymedia:type=story","storyline":[{"id":"6d5f3eec-cf72-3617-b0aa-9bad385893e5","type":"ymedia:type=story"},{"id":"bb14f007-e224-3ea7-95e0-3500c83fd37c","type":"ymedia:type=story"}]},{"id":"467095ee-c921-35a4-a9f5-e04aea96620b","type":"ymedia:type=story"},{"id":"7d20acf9-f1df-32ab-bf94-c0f8a24dc3e6","type":"ymedia:type=story","storyline":[{"id":"69fe12b2-bacb-45f5-9714-1fc1e7b91141","type":"ymedia:type=story"},{"id":"644950d8-6eb3-3811-a898-c1a9e81cdd64","type":"ymedia:type=story"}]},{"id":"cd232e7e-53d5-372e-a824-0ddf1ce16bca","type":"ymedia:type=story","storyline":[{"id":"30013190-f034-3178-a5da-ad48ccf81c6e","type":"ymedia:type=story"},{"id":"48a1c611-9f73-3361-a31b-e2e0484f81ee","type":"ymedia:type=story"}]},{"id":"8b5b1177-4717-396f-9c66-53c789fbb153","type":"ymedia:type=story"},{"id":"1830d8a3-6229-3fbe-ab09-753a3e1ed2cf","type":"ymedia:type=story","storyline":[{"id":"f1371a94-18a7-4a00-a9b9-39f5a9ca8f6b","type":"ymedia:type=story"},{"id":"8b95ec8a-c07f-35c2-ba04-de6f4ac0dc4b","type":"ymedia:type=cavideo"}]},{"id":"857a3c24-6def-3182-95d7-4fd4568c0f76","type":"ymedia:type=story","storyline":[{"id":"84b29407-cc07-334c-a0cc-9f400eb411cf","type":"ymedia:type=story"},{"id":"028ce2d5-d513-3138-97b7-beecc21dd781","type":"ymedia:type=cavideo"}]}],"expId":"megastream_unified__en-US__sports__default__default__desktop__sports_en-us_us_pointwise_dnn_normal__noSplit","sessionId":"2tgldbth88rd7_1652855422622","lastVespaRequestTimestamp":1652855422515,"shouldGridLog":true}}',
                                },
                            },
                        },
                    },
                },
                'ncpRequests': {
                    'RELATED': {
                        'query': {
                            'namespace': 'media',
                            'id': 'related-content-stream',
                            'version': 'v1',
                            'configId': 'contentsim-rc',
                        },
                    },
                },
                'offnet': {
                    'include_lcp': True,
                    'use_preview': True,
                },
                'ss_timeout': 600,
                'useNCP': True,
                'ads': {
                    'ad_polices': True,
                    'carousel': True,
                    'cluster': True,
                    'contentType': 'video/mp4,application/x-shockwave-flash,application/vnd.apple.mpegurl',
                    'count': 25,
                    'enableFlashSale': True,
                    'enableGeminiDealsWithoutBackground': True,
                    'frequency': 4,
                    'geminiPromotionsEnabled': True,
                    'generic_viewability': True,
                    'inline_video': True,
                    'partial_viewability': True,
                    'pu': 'sports.yahoo.com',
                    'se': 5668476,
                    'showTitle': True,
                    'spaceid': '25664825',
                    'start_index': 1,
                    'timeout': 0,
                    'type': 'STRM,STRM_CONTENT,STRM_VIDEO',
                    'useHqImg': True,
                    'useResizedImages': True,
                },
                'batches': {
                    'pagination': True,
                    'size': 10,
                    'timeout': 1000,
                    'total': 120,
                },
                'enableAuthorBio': True,
                'max_exclude': 0,
                'min_count': 3,
                'pnr_package_enabled': True,
                'promoArticle': {
                    'enabled': True,
                    'ctaText': 'Bet on BetMGM',
                    'queryParams': {
                        'promoAdsClusterEnabled': True,
                        'promoAdsClusterImageTags': '190x190|2|80,72x72|2|80',
                        'promoAdsCount': 1,
                        'promoAdsEnabled': True,
                        'promoAdsFrequency': 4,
                        'promoAdsImageTags': '190x190|2|80,72x72|2|80',
                        'promoAdsSectionId': 5682857,
                        'promoAdsStartIndex': 1,
                    },
                },
                'service': {
                    'specRetry': {
                        'enabled': True,
                        'triggerDelayPct': 30,
                        'throttleRate': 100,
                    },
                },
                'sponsoredMomentsAd': {
                    'queryParams': {
                        'smGeminiCluster': False,
                        'smAdBlendInGemini': True,
                    },
                    'where': {
                        'sm_ads_count': 1,
                        'sm_ads_enabled': False,
                        'sm_ads_image_tag': 'img:720x1280',
                        'sm_ads_pu': 'www.yahoo.com',
                        'sm_ads_se': 5661938,
                        'sm_reg_ads_start_index': 1,
                        'sm_ads_start_index': 1,
                        'sm_ads_type': 'STRM,STRM_VIDEO',
                    },
                },
                'pageContext': {
                    'pageType': 'home',
                    'league': 'top',
                    'subPageType': 'home',
                },
            },
        },
    },
    'context': {
        'feature': 'article2_csn,canvassOffnet,enableCMP,enableConsentData,enableYBarFavTeams,sp-nav-test,oathPlayer,enableCCPAFooter,enableReconsent,showFutures,enableUserService,disableCommentsMessage,enableLGPD,watchtogether,enableXrayNcp,enableXrayPeopleSportsEntities,enableXrayTeamEntities,enableXrayTopicEntities,enableAdlite,enableAdLiteUpSellFeedback,enableLeagueDraftOdds,enableLeagueFutures,enableLeagueProps,enableMonalixa3pBodySlot,enableMonalixaBodySlot,enableMonalixaPlacements,enableMonalixaYBarUpsell,enableXrayAthleteHeaderV2,enableXrayNcpV2SalienceMerge,livecoverage,newContentAttribution,caasSmartphone,canvass,desktopNotifications,searchAssist,licensed-only,dfsFavoriteTeamPromo,enableOlyAthletePage,enableGameDriveOdds,yahooDayOne,playerNews,enableMonalixaNcaabBanner,newLogo,sponsoredAds',
        'bkt': [
            'sp_mab_personalized_odds_cntrl',
            'JARVISSPORTSDESKSPEOL04',
        ],
        'crumb': 'L/yDE8AF9QD',
        'device': 'desktop',
        'intl': 'us',
        'lang': 'en-US',
        'partner': 'none',
        'prid': '750068ph894ju',
        'region': 'US',
        'site': 'sports',
        'tz': 'Asia/Japan',
        'ver': '1.0.9127',
        'ecma': 'modern',
    },
}

# 设置代理
proxies = {'http': '114.212.85.117:808', 'https': '114.212.85.117:808'}



iter = 1
for i in range(iter):
    records = json.load(open('./yahoo_sports.json','r'))
    print('当前总新闻数',len(records))
    tmp = {}
    response = requests.post('https://sports.yahoo.com/site/api/resource',proxies=proxies, params=params,  headers=headers, json=json_data)
    print(response.json())
    res = response.json()
    items = res['g0']['data']['stream_items']
    print('爬取：', len(items))
    for item in items:
        try:
            id = item['id']
            record = {'title':item['title'], 'summary':item['summary'], 'url':item['url'], 'category':item['categoryLabel'], 'image':item['images'][list(item['images'].keys())[-1]] }
            tmp.update({id:record})
        except:
            continue
    time.sleep(10)
    print('新增新闻数', len(tmp.keys()))
    records.update(tmp)
    json.dump(records, open('./yahoo_sports.json','w'))
    print('-'*30)