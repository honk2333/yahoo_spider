import requests
import json
import time

cookies = {
    'A1': 'd=AQABBKdthGICEK8hBlDgI5CT3Y34fV-twi4FEgEBAQG_hWKOYgAAAAAA_eMAAA&S=AQAAAlMbDCLi9tFu0fR38Z_nXHE',
    'A3': 'd=AQABBKdthGICEK8hBlDgI5CT3Y34fV-twi4FEgEBAQG_hWKOYgAAAAAA_eMAAA&S=AQAAAlMbDCLi9tFu0fR38Z_nXHE',
    'A1S': 'd=AQABBKdthGICEK8hBlDgI5CT3Y34fV-twi4FEgEBAQG_hWKOYgAAAAAA_eMAAA&S=AQAAAlMbDCLi9tFu0fR38Z_nXHE&j=WORLD',
    'GUC': 'AQEBAQFihb9ijkIhKQSZ',
    'thamba': '2',
    'cmp': 't=1652857057&j=0&u=1---',
    'maex': '%7B%22993a4214%22%3A1652857267%2C%22eafaf0a6%22%3A1652857267%7D',
    '_dd_s': 'logs=1&id=8cb0765e-07fc-47a9-8da0-b9b6ee31d6f3&created=1652857057385&expire=1652858459852',
}

headers = {
    'authority': 'sports.yahoo.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    # Already added when you pass json=
    'content-type': 'application/json',
    # Requests sorts cookies= alphabetically
    'cookie': 'A1=d=AQABBKdthGICEK8hBlDgI5CT3Y34fV-twi4FEgEBAQG_hWKOYgAAAAAA_eMAAA&S=AQAAAlMbDCLi9tFu0fR38Z_nXHE; A3=d=AQABBKdthGICEK8hBlDgI5CT3Y34fV-twi4FEgEBAQG_hWKOYgAAAAAA_eMAAA&S=AQAAAlMbDCLi9tFu0fR38Z_nXHE; A1S=d=AQABBKdthGICEK8hBlDgI5CT3Y34fV-twi4FEgEBAQG_hWKOYgAAAAAA_eMAAA&S=AQAAAlMbDCLi9tFu0fR38Z_nXHE&j=WORLD; GUC=AQEBAQFihb9ijkIhKQSZ; thamba=2; cmp=t=1652857057&j=0&u=1---; maex=%7B%22993a4214%22%3A1652857267%2C%22eafaf0a6%22%3A1652857267%7D; _dd_s=logs=1&id=8cb0765e-07fc-47a9-8da0-b9b6ee31d6f3&created=1652857057385&expire=1652858459852',
    'origin': 'https://sports.yahoo.com',
    'referer': 'https://sports.yahoo.com/news/',
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
    'prid': 'fp6fb5dh896mg',
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
                    'editorial_content_count': 0,
                    'editorial_content_min': 0,
                    'finance_upsell_threshold': 4,
                    'sports_morelink_enabled': True,
                },
                'category': 'LISTID:e6798400-459a-4d3c-84c1-c69909dfcf8f',
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
                                        '69778b5d-5b29-4a71-8e24-56a7619e6800': {
                                            'title': 'What\'s the deal? Why Fox is paying Brady $375M',
                                            'summary': 'Networks seem comfortable investing tens of millions of dollars per year on their top NFL announcing teams when there is little indication they deliver higher ratings.',
                                            'thumbailPhotoId': '326fdd03-4fcf-38e5-879b-cc1965a01f4f',
                                            'list': 'e6798400-459a-4d3c-84c1-c69909dfcf8f',
                                        },
                                        '37683cd0-0100-401c-ac1d-5c3a4be740f5': {
                                            'title': 'Gaudreau nets Game 7 OT winner for Flames',
                                            'summary': 'It took everything they had, but the Flames eventually found a way to squeak by the pesky Stars and their breakout netminder in Game 7.',
                                            'thumbailPhotoId': 'f3c7f00b-77c3-3289-8ae3-8e4d524427ab',
                                            'list': 'e6798400-459a-4d3c-84c1-c69909dfcf8f',
                                        },
                                        'a495bd48-1347-4faf-aea4-5d319a5ec374': {
                                            'title': 'Maybe there\'s hope for \'Hard Knocks\' Lions',
                                            'summary': 'The last five teams featured on the docuseries went a combined 49-32 against the spread.',
                                            'thumbailPhotoId': '59dd226a-a5b0-3fa7-9bc7-159df9eb2472',
                                            'list': 'e6798400-459a-4d3c-84c1-c69909dfcf8f',
                                        },
                                        'c4e06c62-2e18-411e-b083-a4d60f0e7424': {
                                            'title': 'Tatum goes off for 46 to keep Celtics\' season alive',
                                            'summary': 'Giannis Antetokounmpo had an incredible 44-point game, but Jayson Tatum and company weren\'t ready to have their season end just yet as they forced Game 7.',
                                            'thumbailPhotoId': '6a9cd91e-a272-3835-977b-3d9050535b48',
                                            'list': 'e6798400-459a-4d3c-84c1-c69909dfcf8f',
                                        },
                                        '3f63475a-7d61-4830-9943-f5abcf436f18': {
                                            'title': 'Trash talk came back to bite Warriors stars',
                                            'summary': 'Golden State veterans Draymond Green and Stephen Curry managed to enjoy themselves despite the Grizzlies beating the Warriors by 39 points.',
                                            'thumbailPhotoId': '717f872d-3aef-3b42-8f4a-25dbbe5b5529',
                                            'list': 'e6798400-459a-4d3c-84c1-c69909dfcf8f',
                                        },
                                        'f0c753f3-b8fb-34ba-a6c1-23832ff2fea6': {
                                            'title': 'Oilers advance thanks to McDavid\'s dagger',
                                            'summary': 'Connor McDavid had an assist and a goal in the final minutes to seal Edmonton\'s 2-0 win over the Kings in Game 7 of their first-round series.',
                                            'thumbailPhotoId': 'cf1fd8b7-662b-3af8-b249-4e83030bca75',
                                            'list': 'e6798400-459a-4d3c-84c1-c69909dfcf8f',
                                        },
                                        '4bafa216-547f-41e9-90ce-81a6dd1fdcd4': {
                                            'title': 'Jeudy released on bond after domestic dispute',
                                            'summary': 'Judge says Broncos WR Jerry Jeudy does not pose a threat of physical violence to the alleged victim, the mother of his child, ahead of the next court date on May 31.',
                                            'thumbailPhotoId': 'd66b39c6-74ff-30e2-81d7-05c4795ad750',
                                            'list': 'e6798400-459a-4d3c-84c1-c69909dfcf8f',
                                        },
                                        '0df08640-673f-4100-a3fd-9564757cc5aa': {
                                            'title': 'Fickell, Cincinnati continue to break barriers',
                                            'summary': 'Nine NFL draft picks in a single class is an astounding accomplishment for Luke Fickell\'s Bearcats program competing in the AAC with a 40,000-seat stadium.',
                                            'thumbailPhotoId': '78ffeb84-65d9-35be-a262-90a2c8949475',
                                            'list': 'e6798400-459a-4d3c-84c1-c69909dfcf8f',
                                        },
                                        'a8cac02a-3535-425d-84b9-324fbc9de2c9': {
                                            'title': 'Mickelson withdraws from PGA Championship',
                                            'summary': 'Lefty will not defend his PGA Championship title next month.',
                                            'thumbailPhotoId': '8fa5ca77-e1c9-349b-8cc4-8980f5478356',
                                            'list': 'e6798400-459a-4d3c-84c1-c69909dfcf8f',
                                        },
                                        '627762bc-4e5a-4f8a-b141-b4d3c9f191ac': {
                                            'title': 'Let it fly: Celtics look poised to go all the way',
                                            'summary': 'Jayson Tatum and Jaylen Brown are more experienced, role players are contributing in major ways and the resilient Celtics are legitimate championship favorites.',
                                            'thumbailPhotoId': '2ac56b3d-9ca0-3207-95d8-84ae0fa98df9',
                                            'list': 'e6798400-459a-4d3c-84c1-c69909dfcf8f',
                                        },
                                        'ed16ccfc-1be7-4a7c-8f31-2f25f14559b8': {
                                            'title': 'Miami marches on as 76ers crumble in Game 6',
                                            'summary': 'The Heat cruised to a closeout victory in Philadelphia to advance to their second Eastern Conference final in the last three years.',
                                            'thumbailPhotoId': 'b79d4c88-8baf-3772-aa6b-970beb5e9611',
                                            'list': 'e6798400-459a-4d3c-84c1-c69909dfcf8f',
                                        },
                                        '33f453db-5fbd-46ed-8bfe-61d094d5c182': {
                                            'title': 'Reds don\'t allow a hit to Pirates, still lose',
                                            'summary': 'Reds pitchers combined to no-hit the Pirates through eight innings on Sunday, but still managed to lose the game. Here\'s how it all went down.',
                                            'thumbailPhotoId': '0298f3c3-10d3-3945-9117-a1289d6c0471',
                                            'list': 'e6798400-459a-4d3c-84c1-c69909dfcf8f',
                                        },
                                        '08e8a717-a8d5-4dd2-9a2e-f80dbb2cd41c': {
                                            'title': 'Holyfield\'s son upset by literal electrician',
                                            'summary': 'Evan Holyfield was a -10000 favorite to beat Jurmain McDonald on Saturday, but that all changed when McDonald dropped him with a second-round KO.',
                                            'thumbailPhotoId': 'a12524d4-d9bf-3721-94b0-892b4e68ff67',
                                            'list': 'e6798400-459a-4d3c-84c1-c69909dfcf8f',
                                        },
                                        'c488dc11-a332-48f0-a75a-e3f58b1b5e40': {
                                            'title': 'Bills players react to tragic Buffalo mass shooting',
                                            'summary': 'Ten people were killed and three others were wounded in a mass shooting at a Buffalo supermarket on Saturday.',
                                            'thumbailPhotoId': '06b6f4e0-7c78-3adf-b731-6f2b94e4eafa',
                                            'list': 'e6798400-459a-4d3c-84c1-c69909dfcf8f',
                                        },
                                        '011e8d9b-5bcd-4913-9ef4-3e0814019e84': {
                                            'title': 'This NFL sked game leak has plenty of intrigue',
                                            'summary': 'Cowboys coach Mike McCarthy and Packers QB Aaron Rodgers will meet as opponents for the first time since McCarthy was fired by the Packers in 2018.',
                                            'thumbailPhotoId': 'c1d205f5-75b1-3183-8d93-36fcc78d9e29',
                                            'list': 'e6798400-459a-4d3c-84c1-c69909dfcf8f',
                                        },
                                        '31be400f-3244-4ae3-9e2c-df2f6a4bb077': {
                                            'title': 'Nikola Jokic is a worthy NBA MVP, but...',
                                            'summary': 'Let\'s begin by stating the obvious: Nikola Jokic is a worthy MVP, and his two-year run has been nothing short of phenomenal.\n\n',
                                            'thumbailPhotoId': '3507e1b1-f7c2-3338-bd38-390e5fcedc5e',
                                            'list': 'e6798400-459a-4d3c-84c1-c69909dfcf8f',
                                        },
                                        '3833777d-de52-45cb-9ffc-154b0ba85d84': {
                                            'title': 'Can Mavericks, 76ers force Game 7s?',
                                            'summary': 'Home teams have dominated this round of the NBA playoffs. That\'s good news for Dallas and Philly, which look to avoid elimination vs. Phoenix and Miami, respectively.',
                                            'thumbailPhotoId': 'e74de16a-bd55-32fa-a0a1-428f101c3902',
                                            'list': 'e6798400-459a-4d3c-84c1-c69909dfcf8f',
                                        },
                                        '5d003b02-5c55-4a0c-8907-34398e1aa3f7': {
                                            'title': 'Who should you put your money on in East finals?',
                                            'summary': 'Boston took down Milwaukee on Sunday and will play Miami in Game 1 on Tuesday.',
                                            'thumbailPhotoId': '84d149dc-01fa-32b3-bf98-5abc47487ee0',
                                            'list': 'e6798400-459a-4d3c-84c1-c69909dfcf8f',
                                        },
                                        'ddd36b5e-f285-4f55-9abe-bbd802542e99': {
                                            'title': 'Teams get creative with schedule release videos',
                                            'summary': 'From the avant-garde to anime, NFL teams had some fun with schedule release day.',
                                            'thumbailPhotoId': 'bc92d6d6-b52f-3cf1-966f-d86ac99af3c6',
                                            'list': 'e6798400-459a-4d3c-84c1-c69909dfcf8f',
                                        },
                                        'b81183e0-dd17-4628-b860-e8526bcf71f0': {
                                            'title': 'Payton II a \'long shot\' to play in West finals',
                                            'summary': 'Steve Kerr\'s not ready to rule Payton out with a tough backcourt matchup awaiting in the Western Conference finals.',
                                            'thumbailPhotoId': '85f3167f-839a-3ae6-b12b-b62c146e1c6c',
                                            'list': 'e6798400-459a-4d3c-84c1-c69909dfcf8f',
                                        },
                                        '0211c749-1f60-42be-9888-7f81a5d8c7cb': {
                                            'title': 'NFL booth shake-up creates new teams',
                                            'summary': 'Who\'s best? Tirico and Collinsworth, Michaels and Herbstreit, Nantz and Romo, Buck and Aikman, or Burkhardt and Brady (after he retires from playing)?',
                                            'thumbailPhotoId': '98be99a4-e305-3e3a-9859-2221a816a21a',
                                            'list': 'e6798400-459a-4d3c-84c1-c69909dfcf8f',
                                        },
                                        'c8c64337-9164-4d52-8f76-c49456d0a4f8': {
                                            'title': 'Golden Knights fire DeBoer after parts of 3 seasons',
                                            'summary': 'After a disappointing season and driving a wedge with another netminder, Pete DeBoer is out as Vegas\'s head coach.',
                                            'thumbailPhotoId': '948ce4a5-28df-3b80-90a3-520942623dd6',
                                            'list': 'e6798400-459a-4d3c-84c1-c69909dfcf8f',
                                        },
                                        'f2e3a96c-faa9-4844-899f-14450872bc8b': {
                                            'title': 'Embiid \'just knew\' he wasn\'t going to win MVP',
                                            'summary': 'For the second straight year Joel Embiid was edged out by Denver Nuggets big man Nikola Jokic.',
                                            'thumbailPhotoId': '3f9e1598-3f52-3bec-951e-26b55d6ae705',
                                            'list': 'e6798400-459a-4d3c-84c1-c69909dfcf8f',
                                        },
                                        'c877daa4-c2ab-4a9e-a06f-49c3af07f8b5': {
                                            'title': 'Frank Gore wins boxing debut with 1-punch KO',
                                            'summary': 'Frank Gore\'s pro boxing debut could not have gone any better (or ended much quicker) as the ex-NFL RB ended the fight with one punch.',
                                            'thumbailPhotoId': '4d61757d-a193-3f47-853c-502dca9e335a',
                                            'list': 'e6798400-459a-4d3c-84c1-c69909dfcf8f',
                                        },
                                        '2c2be70c-30b5-4c2b-85f8-2b060686f627': {
                                            'title': 'Reenergized Blachowicz back in win column',
                                            'summary': 'Former light heavyweight champ Jan Blachowicz got the TKO win over Aleksandar Rakic due to Rakic\'s leg injury at UFC Vegas 54.',
                                            'thumbailPhotoId': '3bc4e9b7-5f57-3668-a436-9be72839d26b',
                                            'list': 'e6798400-459a-4d3c-84c1-c69909dfcf8f',
                                        },
                                        '3338193a-4be7-487d-a64d-f373d5d4d7a5': {
                                            'title': 'Are Bucks asking too much of Giannis?',
                                            'summary': 'With Khris Middleton out with an injury, Milwaukee\'s hopes rest on reigning NBA Finals MVP Giannis Antetokounmpo\'s shoulders. That didn\'t go well in Game 4.',
                                            'thumbailPhotoId': 'c337682b-2264-3796-ac85-a562f3436bc9',
                                            'list': 'e6798400-459a-4d3c-84c1-c69909dfcf8f',
                                        },
                                        '974e0f74-8e0d-4819-9f9c-54d7de13e1ab': {
                                            'title': 'Russia wants \'Merchant of Death\' in swap for Griner',
                                            'summary': 'Russia is looking to exchange WNBA star Britney Griner in a prisoner swap for notorious convicted arms trafficker Viktor Bout, several state-owned Russian news outlets said.',
                                            'thumbailPhotoId': 'f6590269-b185-37fa-9392-ae11b0563a33',
                                            'list': 'e6798400-459a-4d3c-84c1-c69909dfcf8f',
                                        },
                                        'f9786c65-bb17-4364-9ce1-94080b267007': {
                                            'title': 'Thomas arrested 2 weeks after warrant issued',
                                            'summary': 'Former Seahawks safety Earl Thomas was arrested Friday night in Texas, where he played high school and college football.',
                                            'thumbailPhotoId': '0923bc18-04c3-37f6-992f-084c289f1612',
                                            'list': 'e6798400-459a-4d3c-84c1-c69909dfcf8f',
                                        },
                                        '3677eaba-ad96-3e3b-b92b-a5f5ad2b55f3': {
                                            'title': 'City keeps hand on trophy with frantic comeback',
                                            'summary': 'Manchester City fought back from 2-0 down to draw 2-2 at West Ham as Pep Guardiola\'s side coughed up the chance to win late.',
                                            'thumbailPhotoId': '1b5cca77-c229-3c27-9f9e-786832417c7a',
                                            'list': 'e6798400-459a-4d3c-84c1-c69909dfcf8f',
                                        },
                                        '02bb00c9-1706-49ec-9b67-9d00e7dcd0e3': {
                                            'title': 'Game 6 Klay comes alive as Warriors oust Grizzlies',
                                            'summary': 'Game 6 Klay is back, y\'all.',
                                            'thumbailPhotoId': 'be7adcc8-6cfa-3068-9024-053c06d9cd86',
                                            'list': 'e6798400-459a-4d3c-84c1-c69909dfcf8f',
                                        },
                                        '0a4be700-2814-4591-be6e-3f59e4e1a1f1': {
                                            'title': 'Apparently, Simmons \'likes\' Harden slander ',
                                            'summary': 'Ben Simmons seemed to enjoy watching his former team\'s demise on Thursday, liking a Skip Bayless tweet calling out James Harden\'s poor playoff game.',
                                            'thumbailPhotoId': '7f7e7b89-4264-3542-90f3-9e3254b540e8',
                                            'list': 'e6798400-459a-4d3c-84c1-c69909dfcf8f',
                                        },
                                        '0d8fd949-cc93-48e1-b826-ff77bc68fb27': {
                                            'title': 'Unlikely hero pushes Celtics past Bucks',
                                            'summary': 'Of all the predictions for how Game 7 might play out, Grant Williams leading the Celtics in scoring against the defending champs was not high on anyone\'s list.',
                                            'thumbailPhotoId': '76d85445-529f-36a9-b723-15f695b6af9c',
                                            'list': 'e6798400-459a-4d3c-84c1-c69909dfcf8f',
                                        },
                                        '68f76194-2d02-40f2-b27a-76494d71eff0': {
                                            'title': 'Yelich hits for 3rd career cycle — all vs. the Reds',
                                            'summary': 'Brewers outfielder Christian Yelich is now in a five-way tie for the most cycles by a player in MLB history.',
                                            'thumbailPhotoId': 'b660fc5a-166e-3e8d-a51a-205b483640c2',
                                            'list': 'e6798400-459a-4d3c-84c1-c69909dfcf8f',
                                        },
                                        'b11e2089-8ebb-45d1-9549-679466668ce8': {
                                            'title': 'Butler twists the knife after eliminating 76ers',
                                            'summary': 'After eliminating them from the playoffs, Heat star Jimmy Butler let the 76ers know they should not have let him walk after the 2018-19 season.',
                                            'thumbailPhotoId': 'f9861ebe-81b9-3436-897a-ce95891b136f',
                                            'list': 'e6798400-459a-4d3c-84c1-c69909dfcf8f',
                                        },
                                        '662a5bb9-487b-441f-b868-154817610d75': {
                                            'title': 'Key matchups that could swing Game 7s',
                                            'summary': 'There are five Game 7s this weekend — three on Saturday. Here are  insights and observations as an exciting first round of the NHL playoffs winds down.',
                                            'thumbailPhotoId': 'e94dc14c-1262-35d3-b493-24bc44c9a76c',
                                            'list': 'e6798400-459a-4d3c-84c1-c69909dfcf8f',
                                        },
                                        '0b81b7f6-a2c9-4aad-851f-7da8253514f0': {
                                            'title': '2022 shaping up to be special year for Angels?',
                                            'summary': 'They’ve had stars Mike Trout and Shohei Ohtani, so what changed to make the 2022 team a fun playoff contender?',
                                            'thumbailPhotoId': 'c3531cda-207d-3fb4-815e-e6d602d8e346',
                                            'list': 'e6798400-459a-4d3c-84c1-c69909dfcf8f',
                                        },
                                    },
                                    'remainingCount': 36,
                                    'uuids': 'b81183e0-dd17-4628-b860-e8526bcf71f0:STORY,c8c64337-9164-4d52-8f76-c49456d0a4f8:STORY,627762bc-4e5a-4f8a-b141-b4d3c9f191ac:STORY,5d003b02-5c55-4a0c-8907-34398e1aa3f7:STORY,37683cd0-0100-401c-ac1d-5c3a4be740f5:STORY,c488dc11-a332-48f0-a75a-e3f58b1b5e40:STORY,0d8fd949-cc93-48e1-b826-ff77bc68fb27:STORY,33f453db-5fbd-46ed-8bfe-61d094d5c182:STORY,c877daa4-c2ab-4a9e-a06f-49c3af07f8b5:STORY,3677eaba-ad96-3e3b-b92b-a5f5ad2b55f3:STORY,2c2be70c-30b5-4c2b-85f8-2b060686f627:STORY,08e8a717-a8d5-4dd2-9a2e-f80dbb2cd41c:STORY,f0c753f3-b8fb-34ba-a6c1-23832ff2fea6:STORY,f9786c65-bb17-4364-9ce1-94080b267007:STORY,662a5bb9-487b-441f-b868-154817610d75:STORY,a495bd48-1347-4faf-aea4-5d319a5ec374:STORY,02bb00c9-1706-49ec-9b67-9d00e7dcd0e3:STORY,a8cac02a-3535-425d-84b9-324fbc9de2c9:STORY,974e0f74-8e0d-4819-9f9c-54d7de13e1ab:STORY,c4e06c62-2e18-411e-b083-a4d60f0e7424:STORY,31be400f-3244-4ae3-9e2c-df2f6a4bb077:STORY,4bafa216-547f-41e9-90ce-81a6dd1fdcd4:STORY,0a4be700-2814-4591-be6e-3f59e4e1a1f1:STORY,b11e2089-8ebb-45d1-9549-679466668ce8:STORY,ddd36b5e-f285-4f55-9abe-bbd802542e99:STORY,ed16ccfc-1be7-4a7c-8f31-2f25f14559b8:STORY,0b81b7f6-a2c9-4aad-851f-7da8253514f0:STORY,3f63475a-7d61-4830-9943-f5abcf436f18:STORY,69778b5d-5b29-4a71-8e24-56a7619e6800:STORY,3833777d-de52-45cb-9ffc-154b0ba85d84:STORY,f2e3a96c-faa9-4844-899f-14450872bc8b:STORY,0df08640-673f-4100-a3fd-9564757cc5aa:STORY,68f76194-2d02-40f2-b27a-76494d71eff0:STORY,0211c749-1f60-42be-9888-7f81a5d8c7cb:STORY,3338193a-4be7-487d-a64d-f373d5d4d7a5:STORY,011e8d9b-5bcd-4913-9ef4-3e0814019e84:STORY',
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
                    'spaceid': '25664825',
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
                    'pageType': 'utility',
                    'league': '',
                    'subPageType': 'news',
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
        'prid': 'fp6fb5dh896mg',
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
    print(response.json())
    exit(1)
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