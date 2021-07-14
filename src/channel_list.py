from enum import Enum


class Region(Enum):
    JPN = 1
    CHN = 2
    INA = 3
    ENG = 4
    KOR = 5


channels = {
    # じぶん
    # 'UCK__zbu6IRcAeno4i1E4t7Q': {'name': 'テスト🐝', 'tag': '#はちの生放送', 'region': Region.JPN},

    # 一期生
    'UCD-miitqNY3nyukJ4Fnf4_A': {'name': '月ノ美兎🐰', 'tag': '#みとの生放送', 'region': Region.JPN},
    'UCsg-YqdqQ-KFF0LNk23BY4A': {'name': '樋口楓🍁', 'tag': '#でろおんえあ', 'region': Region.JPN},
    'UC6oDys1BGgBsIC3WhG1BovQ': {'name': '静凛💜', 'tag': '#しずりん生放送 #バーチャル凛', 'region': Region.JPN},
    'UCYKP16oMX9KKPbrNgo_Kgag': {'name': 'える🗼', 'tag': '#えるえる生放送', 'region': Region.JPN},
    'UCLO9QDxVL4bnvRRsz6K4bsQ': {'name': '勇気ちひろ🎀💙', 'tag': '#ちーらいぶ', 'region': Region.JPN},
    'UCvmppcdYf4HOv-tFQhHHJMA': {'name': 'モイラ👼', 'tag': '#もいもいもい', 'region': Region.JPN},
    'UCt9qik4Z-_J-rj3bKKQCeHg': {'name': '鈴谷アキ🐈', 'tag': '#アキ生', 'region': Region.JPN},
    'UCpnvhOIJ6BN-vPkYU9ls-Eg': {'name': '鈴谷アキ🐈', 'tag': '#アキ生', 'region': Region.JPN},
    'UCeK9HFcRZoTrvqcUCtccMoQ': {'name': '渋谷ハジメ🌱', 'tag': '#渋谷ハジメ生放送', 'region': Region.JPN},

    # 二期生
    'UCv1fFr156jc65EMiLbaLImw': {'name': '剣持刀也⚔️', 'tag': '#剣持刀也生', 'region': Region.JPN},
    'UCXU7YYxy_iQd3ulXyO-zC2w': {'name': '伏見ガク🦊', 'tag': '#生アクト', 'region': Region.JPN},
    'UCtpB6Bvhs1Um93ziEDACQ8g': {'name': '森中花咲🐻', 'tag': '#かざ生放送', 'region': Region.JPN},
    'UCBiqkFJljoxAj10SoP2w2Cg': {'name': '文野環🐟', 'tag': '#のらジェット', 'region': Region.JPN},
    'UCmUjjW5zF1MMOhYUwwwQv9Q': {'name': '宇志海いちご🍓', 'tag': '#いちご放送', 'region': Region.JPN},
    'UC48jH1ul-6HOrcSSfoR02fQ': {'name': '夕陽リリ🌇', 'tag': '#リリ生放送', 'region': Region.JPN},
    'UC_GCs6GARLxEHxy1w40d6VQ': {'name': '家長むぎ🌷', 'tag': '#むぎむぎ生放送', 'region': Region.JPN},
    'UCwokZsOK_uEre70XayaFnzA': {'name': '鈴鹿詩子🎶', 'tag': '#詩子おねえさんといっしょ', 'region': Region.JPN},
    'UCUzJ90o1EjqUbk2pBAy0_aw': {'name': 'ギルザレンⅢ世🏰🌑', 'tag': '#ギルザレンIII世', 'region': Region.JPN},
    'UCt0clH12Xk1-Ej5PXKGfdPA': {'name': '♥️♠️物述有栖♦️♣️', 'tag': '#有栖のお茶会', 'region': Region.JPN},

    # SEEDs一期生
    'UC53UDnhAAYwvNO7j_2Ju1cQ': {'name': 'ドーラ🔥', 'tag': '#ドーラとおはなし', 'region': Region.JPN},
    'UCt5-0i4AVHXaWJrL8Wql3mw': {'name': '緑仙🐼', 'tag': '#緑仙', 'region': Region.JPN},
    'UC1zFJrfEKvCixhsjNSb1toQ': {'name': 'シスター・クレア🔔', 'tag': '#たぬさんあつまれ', 'region': Region.JPN},
    'UCKMYISTJAQ8xTplUPHiABlA': {'name': '社築🖥', 'tag': '#社築フィードバック', 'region': Region.JPN},
    'UCsFn_ueskBkMCEyzCEqAOvg': {'name': '花畑チャイカ🌵', 'tag': '#チャイカデラックス', 'region': Region.JPN},
    'UCLpYMk5h1bq8_GAFVBgXhPQ': {'name': '出雲霞🦑', 'tag': '#生カスミ', 'region': Region.JPN},
    'UCRV9d6YCYIMUszK-83TwxVA': {'name': '轟京子🐐', 'tag': '#ろき生', 'region': Region.JPN},
    'UCaF-mODqAziHivqg0Q61XKQ': {'name': '鈴木勝☪️', 'tag': '#漆黒の観測者', 'region': Region.JPN},
    'UCryOPk2GZ1meIDt53tL30Tw': {'name': '鈴木勝☪️', 'tag': '#漆黒の観測者', 'region': Region.JPN},
    'UC6TfqY40Xt1Y0J-N18c85qQ': {'name': '安土桃‏🍑', 'tag': '#ももほうそう', 'region': Region.JPN},
    'UC3lNFeJiTq6L3UWoz4g1e-A': {'name': '卯月コウ🌙', 'tag': '#卯月コウ', 'region': Region.JPN},

    # SEEDs二期生
    'UCV5ZZlLjk5MKGg3L0n0vbzw': {'name': '鷹宮リオン🦅', 'tag': '#リオ生', 'region': Region.JPN},
    'UCJubINhCcFXlsBwnHp0wl_g': {'name': '舞元啓介👨‍🌾', 'tag': '#まいもとなま', 'region': Region.JPN},
    'UCPvGypSgfDkVe7JG2KygK7A': {'name': '竜胆尊🍶⚜', 'tag': '#竜胆尊', 'region': Region.JPN},
    'UCWz0CSYCxf4MhRKPDm220AQ': {'name': '神田笑一🔪🍅', 'tag': '#噛むなよ神田', 'region': Region.JPN},
    'UCiSRx1a2k-0tOg-fs6gAolQ': {'name': '飛鳥ひな🐤', 'tag': '#ことりさん通信', 'region': Region.JPN},
    'UCRWOdwLRsenx2jLaiCAIU4A': {'name': '雨森小夜☂️☔️', 'tag': '#雨森と雨宿り', 'region': Region.JPN},
    'UCP19rQ5V-46B-6ZeLDJqp5w': {'name': 'でびでび・でびる🚪👿', 'tag': '#でびでびるなま', 'region': Region.JPN},
    'UCjlmCrq4TP1I4xguOtJ-31w': {'name': 'でびでび・でびる🚪👿', 'tag': '#でびでびるなま', 'region': Region.JPN},
    'UCfQVs_KuXeNAlGa3fb8rlnQ': {'name': '桜凛月🌸', 'tag': '#生りつきーん', 'region': Region.JPN},
    'UCo7TRj3cS-f_1D9ZDmuTsjw': {'name': '町田ちま🐹', 'tag': '#なま公', 'region': Region.JPN},
    'UCqQV8xEBWd5SVZBLlYrS_5Q': {'name': '月見しずく✨', 'tag': '#お月見時', 'region': Region.JPN},
    'UChUJbHiTVeGrSkTdBzVfNCQ': {'name': 'ジョー・力一🤡🎈', 'tag': '#常套句', 'region': Region.JPN},
    'UCtAvQ5U0aXyKwm2i4GqFgJg': {'name': '春崎エアル🍭', 'tag': '#ハルライブ', 'region': Region.JPN},
    'UCoM_XmK45j504hfUWvN06Qg': {'name': '成瀬鳴🍥', 'tag': '#鳴onlive', 'region': Region.JPN},
    'UCbc8fwhdUNlqi-J99ISYu4A': {'name': 'ベルモンド・バンデラス🥃', 'tag': '#ようこそデラスへ', 'region': Region.JPN},
    'UCvzVB-EYuHFXHZrObB8a_Og': {'name': '矢車りね🌽', 'tag': '#矢車観察日記', 'region': Region.JPN},
    'UCTIE7LM5X15NVugV7Krp9Hw': {'name': '夢追翔🎤', 'tag': '#翔onAir', 'region': Region.JPN},
    'UCmeyo5pRj_6PXG-CsGUuWWg': {'name': '黒井しば🐕🐾', 'tag': '#しばの世話', 'region': Region.JPN},

    # ゲーマーズ
    'UCspv01oxUFf_MTSipURRhkA': {'name': '叶🔫', 'tag': '#かなえーる', 'region': Region.JPN},
    'UCBi8YaVyZpiKWN3_Z0dCTfQ': {'name': '赤羽葉子💀', 'tag': '#赤羽絶況チュウ', 'region': Region.JPN},
    'UC0g1AE0DOjBYnLhkgoRWN1w': {'name': '本間ひまわり🌻', 'tag': '#ひま生', 'region': Region.JPN},
    'UCoztvTULBYd3WmStqYeoHcA': {'name': '笹木咲🎋', 'tag': '#笹らいぶ', 'region': Region.JPN},
    'UC_4tXjqecqox5Uc05ncxpxg': {'name': '椎名唯華👻', 'tag': '#しい生', 'region': Region.JPN},
    'UCSFCh5NL4qXrAy9u-u2lX3g': {'name': '葛葉🎲', 'tag': '#くずなま', 'region': Region.JPN},
    'UC9EjSJ8pvxtvPdxLOElv73w': {'name': '魔界ノりりむ🍼', 'tag': '#りりむとあそぼう', 'region': Region.JPN},

    # '19
    'UCveZ9Ic1VtcXbsyaBgxPMvg': {'name': '童田明治🐺🍎', 'tag': '#めいとひなたぼっこ', 'region': Region.JPN},
    'UCCVwhI5trmaSxfcze_Ovzfw': {'name': '夢月ロア🌖', 'tag': '#ロアゲート', 'region': Region.JPN},
    'UCeShTCVgZyq2lsBW9QwIJcw': {'name': '郡道美玲🐽', 'tag': '#教えて郡道先生', 'region': Region.JPN},
    'UCg63a3lk6PNeWhVvMRM_mrQ': {'name': '小野町春香♨️', 'tag': '#小野町旅館', 'region': Region.JPN},
    'UCufQu4q65z63IgE4cfKs1BQ': {'name': '語部紡🧂📘', 'tag': '#語部屋', 'region': Region.JPN},
    'UCHK5wkevfaGrPr7j3g56Jmw': {'name': '瀬戸美夜子📷💚', 'tag': '#せとみやライブ', 'region': Region.JPN},
    'UCwQ9Uv-m8xkE5PzRc7Bqx3Q': {'name': '御伽原江良🏰🕛', 'tag': '#御伽の国の舞踏会', 'region': Region.JPN},
    'UCXRlIK3Cw_TJIQC5kSJJQMg': {'name': '戌亥とこ🍹', 'tag': '#いぬいどんどんすきになる', 'region': Region.JPN},
    'UCHVXbQzkl3rDfsXWo8xi2qw': {'name': 'アンジュ・カトリーナ⚖', 'tag': '#賢者の時間', 'region': Region.JPN},
    'UCZ1xuCK1kNmn5RzPYIZop3w': {'name': 'リゼ・ヘルエスタ👑', 'tag': '#ヘルエスタ国営放送', 'region': Region.JPN},
    'UC0WwEfE-jOM2rzjpdfhTzZA': {'name': '愛園愛美💕', 'tag': '#愛ライブ', 'region': Region.JPN},
    'UCNW1Ex0r6HsWRD4LCtPwvoQ': {'name': '三枝明那🌶', 'tag': '#三枝全力配信', 'region': Region.JPN},
    'UC_a1ZYZ8ZTXpjg9xUY9sj8w': {'name': '鈴原るる🎨', 'tag': '#すずはライブ', 'region': Region.JPN},
    'UCHX7YpFG8rVwhsHCx34xt7w': {'name': '雪城眞尋🌐💫', 'tag': '#まひろおんらいぶ', 'region': Region.JPN},
    'UCIytNcoz4pWzXfLda0DoULQ': {'name': 'エクス・アルビオ🛡', 'tag': '#生エビ', 'region': Region.JPN},
    'UCtnO2N4kPTXmyvedjGWdx3Q': {'name': 'レヴィ・エリファ🔲', 'tag': '#れゔぃあたんねる', 'region': Region.JPN},
    'UCfipDDn7wY-C-SoUChgxCQQ': {'name': '葉山舞鈴🍃🗻', 'tag': '#生け捕り町おこし', 'region': Region.JPN},
    'UCUc8GZfFxtmk7ZwSO7ccQ0g': {'name': 'ニュイ・ソシエール🎃', 'tag': '#にゅらいぶ', 'region': Region.JPN},
    'UCL34fAoFim9oHLbVzMKFavQ': {'name': '夜見れな❥🎩🐤', 'tag': '#れなのマジックショー', 'region': Region.JPN},
    'UCGYAYLDE7TZiiC8U6teciDQ': {'name': '葉加瀬冬雪⚗', 'tag': '#冬雪ラボ', 'region': Region.JPN},
    'UCmovZ2th3Sqpd00F5RdeigQ': {'name': '加賀美ハヤト🏢', 'tag': '#加賀ミーティング', 'region': Region.JPN},
    'UCb5JxV6vKlYVknoJB8TnyYg': {'name': '黛灰💻💙', 'tag': '#ライブハック', 'region': Region.JPN},
    'UCdpUojq0KWZCN9bxXnZwz5w': {'name': 'アルス・アルマル📕', 'tag': '#アルマルーム', 'region': Region.JPN},
    'UCnRQYHTnRLSF0cLJwMnedCg': {'name': '相羽ういは🍮💎', 'tag': '#ういはいしん', 'region': Region.JPN},
    'UCkIimWZ9gBJRamKF0rmPU8w': {'name': '天宮こころ🎐', 'tag': '#あまみゃらいぶ', 'region': Region.JPN},
    'UCpNH2Zk2gw3JBjWAKSyZcQQ': {'name': 'エリー・コニファー🌲', 'tag': '#エリーの妖精通信', 'region': Region.JPN},
    'UCIG9rDtgR45VCZmYnd-4DUw': {'name': 'ラトナ・プティ🐻💎', 'tag': '#ラトプテ', 'region': Region.JPN},
    'UCHBhnG2G-qN0JrrWmMO2FTA': {'name': 'シェリン・バーガンディ🧐', 'tag': '#シェリンの推理ショー', 'region': Region.JPN},
    'UC8C1LLhBhf_E2IBPLSDJXlQ': {'name': '健屋花那💉💘', 'tag': '#すこやカルテ', 'region': Region.JPN},
    'UC2OacIzd2UxGHRGhdHl1Rhw': {'name': '早瀬走🏃‍♀️💨🚴‍♀️', 'tag': '#早瀬放走中', 'region': Region.JPN},
    'UCwrjITPwG4q71HzihV2C7Nw': {'name': 'フミ🔖', 'tag': '#生フミ', 'region': Region.JPN},
    'UCllKI7VjyANuS1RXatizfLQ': {'name': '山神カルタ🎴', 'tag': '#山神カタル', 'region': Region.JPN},
    'UC9V3Y3_uzU5e-usObb6IE1w': {'name': '星川サラ🌟', 'tag': '#星川観測', 'region': Region.JPN},
    'UCb6ObE-XGCctO3WrjRZC-cw': {'name': 'ルイス・キャミー❤️🦋', 'tag': '#ルイスの予告状', 'region': Region.JPN},
    'UCerkculBD7YLc_vOGrF7tKg': {'name': '魔使マオ💥', 'tag': '#まおんらいぶ', 'region': Region.JPN},
    'UCl1oLKcAq93p-pwKfDGhiYQ': {'name': 'えま★おうがすと', 'tag': '#えまと謁見', 'region': Region.JPN},
    'UC6wvdADTJ88OfIbJYIpAaDA': {'name': '不破湊🥂✨', 'tag': '#フワミナイト', 'region': Region.JPN},
    'UCuvk5PilcvDECU7dDZhQiEw': {'name': '白雪巴👠⛓', 'tag': '#女王のお戯れ #白雪調教中', 'region': Region.JPN},
    'UC1QgXt46-GEvtNjEC1paHnw': {'name': 'グウェル・オス・ガール😎', 'tag': '#グウェルステーション', 'region': Region.JPN},
    'UCfki3lMEF6SGBFiFfo9kvUA': {'name': 'ましろ🧷', 'tag': '#ましろとしゃべる', 'region': Region.JPN},
    'UC-o-E6I3IC2q8sAoAuM6Umg': {'name': '奈羅花✖🍳', 'tag': '#ならおんえあ', 'region': Region.JPN},
    'UCRcLAVTbmx2-iNcXSsupdNA': {'name': '来栖夏芽🐏🎵', 'tag': '#なつめぇ牧場', 'region': Region.JPN},

    # 20年組
    'UCuep1JCrMvSxOGgGhBfJuYw': {'name': 'フレン・E・ルスタリオ🎠', 'tag': '#ルスタリオンエア', 'region': Region.JPN},
    'UCwcyyxn6h9ex4sMXGtpQE_g': {'name': 'メリッサ・キンレンカ🐝', 'tag': '#メリートーク', 'region': Region.JPN},
    'UCmZ1Rbthn-6Jm_qOGjYsh5A': {'name': 'イブラヒム💧', 'tag': '#イブライブ', 'region': Region.JPN},
    'UCGw7lrT-rVZCWHfdG9Frcgg': {'name': '弦月藤士郎🎻🛵', 'tag': '#弦ノ刻', 'region': Region.JPN},
    'UCXW4MqCQn-jCaxlX-nn-BYg': {'name': '長尾景☯', 'tag': '#景成長中', 'region': Region.JPN},
    'UCo2N7C-Z91waaR6lF3LL_jw': {'name': '甲斐田晴🌞', 'tag': '#生き甲斐田', 'region': Region.JPN},
    'UC_82HBGtvwN1hcGeOGHzUBQ': {'name': '空星きらめ🌌', 'tag': '#きらきらいぶ', 'region': Region.JPN},
    'UC69URn8iP4u8D_zUp-IJ1sg': {'name': '金魚坂めいろ🩰', 'tag': '#迷子のめいろちゃん', 'region': Region.JPN},
    'UCe_p3YEuYJb8Np0Ip9dk-FQ': {'name': '朝日南アカネ🦖🎖', 'tag': '#あーこといっしょ', 'region': Region.JPN},
    'UCebT4Aq-3XWb5je1S1FvR_A': {'name': '東堂コハク🍯', 'tag': '#東堂堂々行動中', 'region': Region.JPN},
    'UCkngxfPbmGyGl_RIq4FA3MQ': {'name': '西園チグサ🐬🌱', 'tag': '#チグサリウム', 'region': Region.JPN},
    'UCL_O_HXgLJx3Auteer0n0pA': {'name': '周央サンゴ💞🦩', 'tag': '#さんごしょー', 'region': Region.JPN},
    'UCRqBKoKuX30ruKAq05pCeRQ': {'name': '北小路ヒスイ❇️', 'tag': '#ヒストリーム', 'region': Region.JPN},

    # nijisanji id
    'UCA3WE2WRSpoIvtnoVGq4VAw': {'name': 'ZEA Corneliaa🔶', 'tag': '#ZEA_live', 'region': Region.INA},
    'UCZ5dNZsqBjBzbBl0l_IdmXg': {'name': 'Taka Radjiman🥩', 'tag': '#Taka_Live', 'region': Region.INA},
    'UCpJtk0myFr5WnyfsmnInP-w': {'name': 'Hana Macchia☕', 'tag': '#hana_live', 'region': Region.INA},
    'UCOmjciHZ8Au3iKMElKXCF_g': {'name': 'Miyu Ottavia✌️', 'tag': '#miyu_live', 'region': Region.INA},
    'UCkL9OLKjIQbKk2CztbpOCFg': {'name': 'Riksa Dhirendra💥', 'tag': '#riksa_live', 'region': Region.INA},
    'UCrR7JxkbeLY82e8gsj_I0pQ': {'name': 'Amicia Michella🐧', 'tag': '#Amicia_Live', 'region': Region.INA},
    'UC8Snw5i4eOJXEQqURAK17hQ': {'name': 'Rai Galilei🚨', 'tag': '#Rai_Live', 'region': Region.INA},
    'UCyRkQSuhJILuGOuXk10voPg': {'name': 'Layla Alstroemeria🕰🌺', 'tag': '#Layla_live', 'region': Region.INA},
    'UCoWH3sDpeXG1aXmOxveX4KA': {'name': 'Nara Haramaung🐯', 'tag': '#Nara_Live', 'region': Region.INA},
    'UCk5r533QVMgJUdWwqegH2TA': {'name': 'Azura Cecillia👽', 'tag': '#Azura_Live', 'region': Region.INA},
    'UCjFu-9GHnabzSFRAYm1B9Dw': {'name': 'Etna Crimson🌋🍔', 'tag': '#Etna_Live', 'region': Region.INA},
    'UC5qSx7KzdRwbsO1QmJc4d-w': {'name': 'Siska Leontyne🔦🦁', 'tag': '#Siska_live', 'region': Region.INA},
    'UCHjeZylSgXDSnor8wUnwU_g': {'name': 'Bonnivier Pranaja🎣', 'tag': '#bonnivier_live', 'region': Region.INA},

    # nijisanji en
    'UC_aB_-PHLFHiP61djM0oOiQ': {'name': 'Aadya🌸', 'tag': '', 'region': Region.ENG},
    'UC6oW4FXETgEGOFTxWmI2h5Q': {'name': 'Noor💎', 'tag': '', 'region': Region.ENG},
    'UC0lik9pHju6ONgkBh7N5wHw': {'name': 'Vihaan', 'tag': '', 'region': Region.ENG},
    'UC-JSeFfovhNsEhftt1WHMvg': {'name': 'NIJISANJI English Official', 'tag': '', 'region': Region.ENG},

    # nijisanji kr
    'UCzMAP-oh5-pC8j6RlCPf26w': {'name': '위피/Wiffy📶', 'tag': '#온위피 #OnWiffy', 'region': Region.KOR},
    'UCIJ9zP6gIkT8BB4Lz4UYPhA': {'name': '유루리/Ruri Yu🎀🧸', 'tag': '#ruri_live', 'region': Region.KOR},
    'UCjGE11ZnF0JSR8egVAwh-3A': {'name': '신유야/Yuya Shin🌙', 'tag': '#yuyair', 'region': Region.KOR},
    'UCUtKkGKef8BYMs3h-3zQm9A': {'name': '민수하/Suha Min🌊', 'tag': '#suha_live', 'region': Region.KOR},
    'UCZgRRTDMYwHpQ7sCl0aCp2Q': {'name': '카엔/Kaen🦴🔔', 'tag': '#kingkaenlive', 'region': Region.KOR},
    'UCLSzgV37Dt24T8p3-TNiSLg': {'name': '로로/LOROU🎵', 'tag': '', 'region': Region.KOR},
    'UCJ6LH4jMNy0JN9RSThz1mMQ': {'name': '🌑한치호/Chiho Han🦋', 'tag': '#ChihoLive', 'region': Region.KOR},
    'UC6WU2SrnG019ucm_bdY6qxQ': {'name': '☁️백연/Hakuren🌫️', 'tag': '#HakurenLive', 'region': Region.KOR},
    'UCpRXCTyNNa-MnjhK6gisnRw': {'name': '모가온/Gaon👔', 'tag': '#GaonLive', 'region': Region.KOR},
    'UCmWqYB6y8gSfPONWGspuOWQ': {'name': '채아라/Ara Chae🌹💛', 'tag': '#Ara_Live', 'region': Region.KOR},
    'UCSlv7Z-4q7_7NRkzJB10A5Q': {'name': '이시우/Siu Lee🐾', 'tag': '#SIU_SeeU', 'region': Region.KOR},
    'UC5ek2GWKvUKFgnKSHuuCFrw': {'name': '소나기/Nagi So🌧️', 'tag': '#nagilive', 'region': Region.KOR},
    'UC7hffDQLKIEG-_zoAQkMIvg': {'name': '아키라 레이/Akira Ray😸', 'tag': '#Ray_live', 'region': Region.KOR},
    'UC1ZV7KBscK0EMoJKFu1DnDg': {'name': '눈보라/Nun Bora❄️💜', 'tag': '#Nunbo_live', 'region': Region.KOR},
    'UCClwIqTUn5LDpFucHyaAhHg': {'name': '이로하/LeeRoHa🔰', 'tag': '#Roha_Live', 'region': Region.KOR},

    # にじさんじネットワーク
    'UCZYyhgoV314CM14zBD6vd4A': {'name': '天開司🎲', 'tag': '#天開司', 'region': Region.JPN},
    'UC2Rr7mILebYLTjd38DNNUTw': {'name': 'ふぇありす🐦', 'tag': '', 'region': Region.JPN},

    # いちから
    'UCrMDG3r3jzPTJ57P0ZF9e3Q': {'name': '田角陸😇', 'tag': '#リク生', 'region': Region.JPN},
    'UCGCb4Dts1uYtciya3wvd6dg': {'name': 'いわながちゃん🌖', 'tag': '', 'region': Region.JPN},
    'UCX7YkU9nEeaoZbkVLVajcMg': {'name': 'にじさんじ公式🌈🕒', 'tag': '', 'region': Region.JPN},
    'UCz6vnIbgiqFT9xUcD6Bp65Q': {'name': 'ChroNoiR🔫🎲', 'tag': '', 'region': Region.JPN},
    'UC_D2DNy-KUNQJ_NGMppgmyg': {'name': 'JuvveL💎', 'tag': '', 'region': Region.JPN},
}
