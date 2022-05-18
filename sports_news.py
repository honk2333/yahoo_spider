import requests
import json
import time

cookies = {
    'A1': 'd=AQABBKdthGICEK8hBlDgI5CT3Y34fV-twi4FEgEBAQG_hWKOYgAAAAAA_eMAAA&S=AQAAAlMbDCLi9tFu0fR38Z_nXHE',
    'A3': 'd=AQABBKdthGICEK8hBlDgI5CT3Y34fV-twi4FEgEBAQG_hWKOYgAAAAAA_eMAAA&S=AQAAAlMbDCLi9tFu0fR38Z_nXHE',
    'A1S': 'd=AQABBKdthGICEK8hBlDgI5CT3Y34fV-twi4FEgEBAQG_hWKOYgAAAAAA_eMAAA&S=AQAAAlMbDCLi9tFu0fR38Z_nXHE&j=WORLD',
    'GUC': 'AQEBAQFihb9ijkIhKQSZ',
    'thamba': '2',
    'maex': '%7B%22993a4214%22%3A1652875115%2C%22eafaf0a6%22%3A1652875115%7D',
    'cmp': 't=1652875774&j=0&u=1---',
    '_dd_s': 'logs=1&id=d42f9662-b342-4638-a06a-e5684f915509&created=1652876122827&expire=1652877177053',
}

headers = {
    'authority': 'sports.yahoo.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    # Already added when you pass json=
    'content-type': 'application/json',
    # Requests sorts cookies= alphabetically
    'cookie': 'A1=d=AQABBKdthGICEK8hBlDgI5CT3Y34fV-twi4FEgEBAQG_hWKOYgAAAAAA_eMAAA&S=AQAAAlMbDCLi9tFu0fR38Z_nXHE; A3=d=AQABBKdthGICEK8hBlDgI5CT3Y34fV-twi4FEgEBAQG_hWKOYgAAAAAA_eMAAA&S=AQAAAlMbDCLi9tFu0fR38Z_nXHE; A1S=d=AQABBKdthGICEK8hBlDgI5CT3Y34fV-twi4FEgEBAQG_hWKOYgAAAAAA_eMAAA&S=AQAAAlMbDCLi9tFu0fR38Z_nXHE&j=WORLD; GUC=AQEBAQFihb9ijkIhKQSZ; thamba=2; maex=%7B%22993a4214%22%3A1652875115%2C%22eafaf0a6%22%3A1652875115%7D; cmp=t=1652875774&j=0&u=1---; _dd_s=logs=1&id=d42f9662-b342-4638-a06a-e5684f915509&created=1652876122827&expire=1652877177053',
    'origin': 'https://sports.yahoo.com',
    'referer': 'https://sports.yahoo.com/fantasy/',
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
    'prid': 'crn970dh89orf',
    'region': 'US',
    'site': 'sports',
    'tz': 'Asia/Singapore',
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
                    'editorial_content_min': 0,
                    'finance_upsell_threshold': 4,
                    'roundup': True,
                    'sports_morelink_enabled': True,
                },
                'category': 'LISTID:f6505ff8-746d-4bed-9072-2319f34580bf',
                'forceJpg': True,
                'releasesParams': {
                    'limit': 20,
                    'offset': 0,
                },
                'ncpParams': {
                    'query': {
                        'mabEnabled': True,
                        'mabContentEnabled': True,
                        'configId': 'non-personalized',
                        'namespace': 'sports',
                    },
                    'body': {
                        'gqlVariables': {
                            'main': {
                                'pagination': {
                                    'requestedCount': 10,
                                    'contentOverrides': {
                                        '995c4380-c9b8-3dc5-b1ac-0757a6629246': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '5d691c7c-0ed2-4068-9488-cd3757f5b705': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        'a41a38f9-9e69-3c4c-9226-1e6a846e4826': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        'b571148b-4303-4446-98d0-dcfd60efea96': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        'f2fb8ee1-8311-42a1-9e42-cce1c91e1cb0': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '7d0f24fb-4005-4331-bd0d-19cca860bd97': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '9b36850c-ea81-4230-b397-1e720d043801': {
                                            'title': 'Podcast: Early football sleepers and Bruce Arians\' sudden retirement',
                                            'summary': 'Andy Behrens and Scott Pianowski go through the list of guys at each position that they’re targeting in early best ball drafts before their ADP climbs this summer. Which QB will be the next Jalen Hurts? Who will be the new #1 WR in Green Bay? Which fantasy TE did everyone forget about after he missed last season?',
                                            'imageHeight': '1080',
                                            'imageWidth': '1920',
                                            'imageUrl': 'https://s.yimg.com/os/creatr-uploaded-images/2022-03/2090c0e0-b145-11ec-be77-c84d32a801f8',
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '25adaf93-6b41-3d25-87d9-ee03c1fccca7': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        'a27d5222-94f0-31b1-add9-6bdf98ec53d3': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '5c630acc-9821-44d7-8bd0-b3780cf677c6': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '492ce63b-88f5-4e96-8a40-22b7f0974050': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        'e6c547b1-3139-406f-ac76-f0a52f7cb1fa': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '701a1079-b624-3b20-a43a-ef3d162ec48a': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        'e1a15a31-6867-43fe-8850-20cc0ec725b7': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        'ebfeaccf-c04c-4d5d-8d13-ed7bd4f7c98f': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        'd7f1b7b0-4d02-4ce3-be21-02c3247aa0c1': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        'ff4ce848-4d73-4058-be90-e22d405400f3': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '5470beb3-83ee-35ec-9196-988471ae311d': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '2112e29f-c774-3ccf-883a-e37defdb8336': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '739df816-2a33-3450-8e8c-6b69550af417': {
                                            'title': 'Fantasy Baseball Week Ahead: The Mighty Mariner goes twice',
                                            'summary': 'Seth Trachtman looks at next week\'s two-start fantasy pitchers, including young Mariners ace Logan Gilbert.',
                                            'imageHeight': '1132',
                                            'imageWidth': '2016',
                                            'imageUrl': 'https://media.zenfs.com/en/rotoworld.com/a321304e8bf9e8280f0cff83e98a0dce',
                                            'thumbailPhotoId': 'd22cff1e-44c7-30ee-8497-1b6fafb07916',
                                            'scheduled_start': '2022-04-23T15:00:00Z',
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        'fe05562e-24d2-4090-a1e2-f6c7e0c6d193': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '8b13b16a-7d0c-41ff-baf8-be4869fc0b40': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '13a5acc0-5016-4876-9c4e-c4c993a32328': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '66a59ba9-73e0-43f5-a550-0e48c4f87632': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '318abeb5-f201-424a-94b5-0b38278567de': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '83fce051-2f99-4519-b927-d00b9d34a4f9': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '95980ebd-9168-3c9e-ad43-19bb3f7b14c0': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '59b91208-9013-3d1f-a350-b443a49fd326': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '61b3baa8-571b-473b-afb3-2254d35ab55f': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '9ec62a3c-9676-43c1-98e7-a6727ea60f46': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '3dfdaa58-dea1-3aac-9a1e-20aec1ff07ec': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '5c92ec25-0be4-3122-94ab-10106d33e648': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        'a03551bb-714b-4724-ae7e-8be1a16dc55a': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '7ced52d6-d01e-4914-9987-c0dcd6cd3a61': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        'ba1f6ce4-8580-4c6b-b666-e8d7dd76918d': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        'db641157-4fd3-3747-98d7-efcbe48884b0': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '9fd9c156-6d57-44eb-bfe4-962f7c0eebe6': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '4f484ee6-6abd-4a29-8616-0faaf7c239d7': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '2895318e-be5b-37b8-aea8-7d3e6bc9756f': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        'd8b82f00-94ec-45b6-ab3e-7302f00ff92f': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        'f3267660-126f-39a1-acd2-88d0beaadcfe': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        'cb3acd59-32f3-48d2-9a8f-8d992bae601a': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '12a9f009-943c-48cb-b712-f1acb0d4c677': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '33fded20-f7a9-3ac2-889b-4d847ad13579': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '73880253-928e-4f32-b7ae-4b334f3a2f63': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '8511a43f-6cbc-4c8c-ac48-14c4d554dc34': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '783eb28e-ae61-452c-9d28-413a46a2bc95': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        'c98b5a1a-1a4a-47aa-917b-f724617aabb8': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '775a4889-1fbe-4f0e-9efe-7b6c5c28d475': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        'f0879b40-9afd-4e5c-a203-4fa3d0f88a4e': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '7139ccf7-24c6-4a74-98ab-13768597614f': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        'e7c7010c-1d75-4a6a-ab79-168199be55d4': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        'cc6398f3-ebbf-3304-ad9f-1f8da0a42b56': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '5d447707-2969-4ed8-9f6d-faa4d905213f': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '7cfaa993-8f6f-489e-9f81-1ceb98712313': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '612338fe-9166-37f5-aded-3f931f05c950': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '4a76164b-fefb-4eb7-afde-13d593e8fbc4': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '6d167ef2-4370-4420-a51d-d8a4811d26f5': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '003bc928-ef4b-3ea0-8cff-4c22f458a79c': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        'c84bec52-bcb6-4fa5-ac53-572d090129dc': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '9ad5daf4-3a2a-4635-9caa-250568a78f15': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        'aed54ba5-3915-4dc8-886c-abec5b5e02a1': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        'f81d5af8-b8a2-4860-9852-c8bb65fcaedd': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '6616109c-8fd7-4e7f-976b-030f1fa541b3': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '666338d9-8fcf-41b1-bbd8-9fdfd969c321': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '868bfd46-0a1f-33c2-b18b-16e4ebc051bd': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '55e46077-e87d-3fe7-b8f8-31533e0474ff': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '41ab5dd9-485b-4f82-b4c0-00fc7a3d3cd3': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        'a157d0f0-edc5-42da-a855-035439d8fb68': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '8643b2cc-69be-4ee5-9a56-3ebcb258882b': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        'e43d6c2c-0657-4e41-a130-32f7402e7831': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        'ee621475-378d-441d-891b-47f3cbec7133': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        'b9dc846b-e2b8-47a7-af95-3a1fdde6f555': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        'b6400514-fb25-441a-909c-7dec78e45d48': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '2ac84c62-95d3-4bae-aa42-fb812f3dc5d6': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '45aa8005-ed78-44fa-92c5-d5f46fca1f07': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '9d6583fe-808d-43a8-8914-dfef35c834f0': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        'e40fd3b3-2ea2-48c9-b8e6-e4796e8f242e': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '458d590e-9965-475a-8846-a1712b81abe4': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '0eb53535-7588-4179-944a-3aadaf6ae976': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        'cb223a5b-5db7-4074-be34-613f9328b2d4': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '0bced0c9-b7d9-465a-9920-48e7d7afa463': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '1bd714c9-b750-48f3-a44e-fdfc05e4c2df': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '4d52308d-4dc1-4cb6-b5b1-d5574fbcdbfc': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '9e696775-bb9b-4dbb-ae24-82d402dc2f7c': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '4999c1b9-b6fc-38fc-92fe-3e72a3d3d041': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '94993231-ba5e-4b47-b1ce-b2c01f63ef57': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '954aa17d-bb90-49d7-8270-ec94298a8501': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '6f8b3046-c084-4770-bb5a-19f95478a76a': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        'b5f3775b-aec6-4994-939a-6de22f459254': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '87a2bfcc-50b6-4463-b43a-56cee4c4f717': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '8f0d751c-dc6c-35d0-8cb3-e3e568792e6e': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        'c205d128-27c8-3c09-bd18-268cb77947b8': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        'b76177a2-27f2-4483-8b30-7d1834841ee8': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        'eb3edb01-4312-4ccb-b4c9-8aa9d2ba8b5f': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '57d03862-bd6d-4095-a365-cc018ad08dc8': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '5c11d94d-6cbd-3a5a-bc37-ba5b4321a17b': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '95d2d02f-67ab-3115-9346-16b58274e55f': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        '424e6e92-e77d-48a2-95e2-c883539de76f': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                        'a83cb1b4-5c30-4a42-89d7-31b8934a510d': {
                                            'list': 'f6505ff8-746d-4bed-9072-2319f34580bf',
                                        },
                                    },
                                    'remainingCount': 100,
                                    'uuids': '2895318e-be5b-37b8-aea8-7d3e6bc9756f:VIDEO,9ad5daf4-3a2a-4635-9caa-250568a78f15:STORY,cb3acd59-32f3-48d2-9a8f-8d992bae601a:STORY,55e46077-e87d-3fe7-b8f8-31533e0474ff:VIDEO,33fded20-f7a9-3ac2-889b-4d847ad13579:VIDEO,5c630acc-9821-44d7-8bd0-b3780cf677c6:STORY,41ab5dd9-485b-4f82-b4c0-00fc7a3d3cd3:STORY,c205d128-27c8-3c09-bd18-268cb77947b8:VIDEO,9ec62a3c-9676-43c1-98e7-a6727ea60f46:STORY,612338fe-9166-37f5-aded-3f931f05c950:VIDEO,d7f1b7b0-4d02-4ce3-be21-02c3247aa0c1:STORY,003bc928-ef4b-3ea0-8cff-4c22f458a79c:VIDEO,7cfaa993-8f6f-489e-9f81-1ceb98712313:STORY,61b3baa8-571b-473b-afb3-2254d35ab55f:STORY,9b36850c-ea81-4230-b397-1e720d043801:STORY,954aa17d-bb90-49d7-8270-ec94298a8501:STORY,739df816-2a33-3450-8e8c-6b69550af417:STORY,25adaf93-6b41-3d25-87d9-ee03c1fccca7:VIDEO,94993231-ba5e-4b47-b1ce-b2c01f63ef57:STORY,a83cb1b4-5c30-4a42-89d7-31b8934a510d:STORY,aed54ba5-3915-4dc8-886c-abec5b5e02a1:STORY,6d167ef2-4370-4420-a51d-d8a4811d26f5:STORY,458d590e-9965-475a-8846-a1712b81abe4:STORY,b76177a2-27f2-4483-8b30-7d1834841ee8:STORY,87a2bfcc-50b6-4463-b43a-56cee4c4f717:STORY,5c92ec25-0be4-3122-94ab-10106d33e648:VIDEO,a27d5222-94f0-31b1-add9-6bdf98ec53d3:VIDEO,9d6583fe-808d-43a8-8914-dfef35c834f0:STORY,f81d5af8-b8a2-4860-9852-c8bb65fcaedd:STORY,2112e29f-c774-3ccf-883a-e37defdb8336:STORY,8b13b16a-7d0c-41ff-baf8-be4869fc0b40:STORY,5470beb3-83ee-35ec-9196-988471ae311d:STORY,f3267660-126f-39a1-acd2-88d0beaadcfe:STORY,783eb28e-ae61-452c-9d28-413a46a2bc95:STORY,a157d0f0-edc5-42da-a855-035439d8fb68:STORY,95d2d02f-67ab-3115-9346-16b58274e55f:VIDEO,f0879b40-9afd-4e5c-a203-4fa3d0f88a4e:STORY,b5f3775b-aec6-4994-939a-6de22f459254:STORY,9e696775-bb9b-4dbb-ae24-82d402dc2f7c:STORY,66a59ba9-73e0-43f5-a550-0e48c4f87632:STORY,868bfd46-0a1f-33c2-b18b-16e4ebc051bd:VIDEO,ebfeaccf-c04c-4d5d-8d13-ed7bd4f7c98f:STORY,7ced52d6-d01e-4914-9987-c0dcd6cd3a61:STORY,4a76164b-fefb-4eb7-afde-13d593e8fbc4:STORY,1bd714c9-b750-48f3-a44e-fdfc05e4c2df:STORY,fe05562e-24d2-4090-a1e2-f6c7e0c6d193:STORY,424e6e92-e77d-48a2-95e2-c883539de76f:STORY,775a4889-1fbe-4f0e-9efe-7b6c5c28d475:STORY,3dfdaa58-dea1-3aac-9a1e-20aec1ff07ec:VIDEO,318abeb5-f201-424a-94b5-0b38278567de:STORY,5c11d94d-6cbd-3a5a-bc37-ba5b4321a17b:STORY,e43d6c2c-0657-4e41-a130-32f7402e7831:STORY,4f484ee6-6abd-4a29-8616-0faaf7c239d7:STORY,8511a43f-6cbc-4c8c-ac48-14c4d554dc34:STORY,b6400514-fb25-441a-909c-7dec78e45d48:STORY,eb3edb01-4312-4ccb-b4c9-8aa9d2ba8b5f:STORY,6f8b3046-c084-4770-bb5a-19f95478a76a:STORY,83fce051-2f99-4519-b927-d00b9d34a4f9:STORY,7d0f24fb-4005-4331-bd0d-19cca860bd97:STORY,cc6398f3-ebbf-3304-ad9f-1f8da0a42b56:VIDEO,13a5acc0-5016-4876-9c4e-c4c993a32328:STORY,6616109c-8fd7-4e7f-976b-030f1fa541b3:STORY,d8b82f00-94ec-45b6-ab3e-7302f00ff92f:STORY,2ac84c62-95d3-4bae-aa42-fb812f3dc5d6:STORY,9fd9c156-6d57-44eb-bfe4-962f7c0eebe6:STORY,db641157-4fd3-3747-98d7-efcbe48884b0:STORY,59b91208-9013-3d1f-a350-b443a49fd326:VIDEO,0eb53535-7588-4179-944a-3aadaf6ae976:STORY,12a9f009-943c-48cb-b712-f1acb0d4c677:STORY,666338d9-8fcf-41b1-bbd8-9fdfd969c321:STORY,e40fd3b3-2ea2-48c9-b8e6-e4796e8f242e:STORY,45aa8005-ed78-44fa-92c5-d5f46fca1f07:STORY,95980ebd-9168-3c9e-ad43-19bb3f7b14c0:STORY,57d03862-bd6d-4095-a365-cc018ad08dc8:STORY,b571148b-4303-4446-98d0-dcfd60efea96:STORY,73880253-928e-4f32-b7ae-4b334f3a2f63:STORY,c84bec52-bcb6-4fa5-ac53-572d090129dc:STORY,7139ccf7-24c6-4a74-98ab-13768597614f:STORY,a03551bb-714b-4724-ae7e-8be1a16dc55a:STORY,f2fb8ee1-8311-42a1-9e42-cce1c91e1cb0:STORY,c98b5a1a-1a4a-47aa-917b-f724617aabb8:STORY,995c4380-c9b8-3dc5-b1ac-0757a6629246:VIDEO,ff4ce848-4d73-4058-be90-e22d405400f3:STORY,5d691c7c-0ed2-4068-9488-cd3757f5b705:STORY,b9dc846b-e2b8-47a7-af95-3a1fdde6f555:STORY,e6c547b1-3139-406f-ac76-f0a52f7cb1fa:STORY,701a1079-b624-3b20-a43a-ef3d162ec48a:STORY,4d52308d-4dc1-4cb6-b5b1-d5574fbcdbfc:STORY,a41a38f9-9e69-3c4c-9226-1e6a846e4826:VIDEO,4999c1b9-b6fc-38fc-92fe-3e72a3d3d041:VIDEO,492ce63b-88f5-4e96-8a40-22b7f0974050:STORY,e7c7010c-1d75-4a6a-ab79-168199be55d4:STORY,e1a15a31-6867-43fe-8850-20cc0ec725b7:STORY,8f0d751c-dc6c-35d0-8cb3-e3e568792e6e:VIDEO,8643b2cc-69be-4ee5-9a56-3ebcb258882b:STORY,0bced0c9-b7d9-465a-9920-48e7d7afa463:STORY,ba1f6ce4-8580-4c6b-b666-e8d7dd76918d:STORY,cb223a5b-5db7-4074-be34-613f9328b2d4:STORY,ee621475-378d-441d-891b-47f3cbec7133:STORY,5d447707-2969-4ed8-9f6d-faa4d905213f:STORY',
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
                    'spaceid': '782200249',
                    'start_index': 1,
                    'timeout': 0,
                    'type': 'STRM,STRM_CONTENT,STRM_VIDEO',
                    'useHqImg': True,
                    'useResizedImages': True,
                },
                'batches': {
                    'pagination': True,
                    'size': 100,
                    'timeout': 1000,
                    'total': 1200,
                },
                'enableAuthorBio': True,
                'max_exclude': 0,
                'min_count': 3,
                'no_ss_pnr_ntk': True,
                'pnr_package_enabled': True,
                'service': {
                    'specRetry': {
                        'enabled': True,
                        'triggerDelayPct': 30,
                        'throttleRate': 100,
                    },
                },
                'subsite': 'fantasy',
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
                    'pageType': 'minihome',
                    'league': 'fantasy',
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
        'prid': 'crn970dh89orf',
        'region': 'US',
        'site': 'sports',
        'tz': 'Asia/Singapore',
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
    # print(response.json())
    # exit(1)
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
    # time.sleep(10)
    print('过滤后得到的：', len(tmp.keys()))
    records.update(tmp)
    print('更新后总新闻数：', len(records))
    json.dump(records, open('./yahoo_sports.json','w'))
    print('-'*30)