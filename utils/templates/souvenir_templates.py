def category():
    data = [
        {
            "type": "text",
            "text": "気になるお土産のカテゴリーを以下のクイックリプライから選択してください。",
            "quickReply": {
                "items":[
                    {
                        "type": "action",
                        "action": {
                            "type": "message",
                            "label": "焼き菓子",
                            "text": "4-1香川県の焼き菓子のお土産"
                        }
                    },
                    {
                        "type": "action",
                        "action": {
                            "type": "message",
                            "label": "和菓子",
                            "text": "4-2香川県の和菓子のお土産"
                        }
                    },
                    {
                        "type": "action",
                        "action": {
                            "type": "message",
                            "label": "麺類",
                            "text": "4-3香川県の麺類のお土産"
                        }
                    },
                    {
                        "type": "action",
                        "action": {
                            "type": "message",
                            "label": "飲み物",
                            "text": "4-4香川県の飲み物のお土産"
                        }
                    },
                    {
                        "type": "action",
                        "action": {
                            "type": "message",
                            "label": "調味料・食品",
                            "text": "4-5香川県の調味料・食品のお土産"
                        }
                    },
                    {
                        "type": "action",
                        "action": {
                            "type": "message",
                            "label": "骨付きどり",
                            "text": "4-6香川県の骨付きどりのお土産"
                        }
                    },{
                        "type": "action",
                        "action": {
                            "type": "message",
                            "label": "スナック菓子",
                            "text": "4-7香川県のスナック菓子のお土産"
                        }
                    },
                ]
            }
        }
    ]
    return data

def souvenir():
    data = [["1", "讃岐おんまい", "1", "焼き菓子", "1080", "https://shop.cake-cake.net/lowe/select_item.phtml?CATE3_ID=38&_ga=2.167974241.133369611.1692711660-1447591952.1692711660"],
            ["2", "銘菓観音寺", "2", "和菓子", "600", "https://hakueido.jp/phone"],
            ["3", "瀬戸内レモンケーキ", "1", "焼き菓子", "1404", "https://www.la-famille.co.jp/c/gr05/lemoncake"],
            ["4", "かまどパイ", "1", "焼き菓子", "1260", "https://kamado.jp/products/%E3%81%8B%E3%81%BE%E3%81%A9%E3%83%91%E3%82%A4"],
            ["5", "まめまめびーる", "4", "飲み物", "5500", "https://mamemamebeer.thebase.in/"],
            ["6", "幸せの黄色いプリン", "2", "和菓子", "3500", "https://www.shima-life.jp/SHOP/202003005.html"],
            ["7", "スナックさぬきあげうどん", "3", "麵類", "410", "https://www.amazon.co.jp/%E3%83%9E%E3%83%AB%E3%82%B7%E3%83%B3-%E3%81%95%E3%81%AC%E3%81%8D%E3%81%82%E3%81%92%E3%81%86%E3%81%A9%E3%82%93-%E6%97%A8%E5%A1%A9%E5%91%B3-120g%C3%972%E8%A2%8B%E3%82%BB%E3%83%83%E3%83%88/dp/B08NPLCC1Y?&linkCode=ll1&tag=marushin0c-22&linkId=d9602b3aed2af508ee45d2cf38e65843&language=ja_JP&ref_=as_li_ss_tl"],
            ["8", "クアトロえびチーズ", "7", "スナック菓子", "550", "https://www.quattro-ebicheese.com/shopping01.html#listarea"],
            ["9", "プレミアムクリームチーズスプレッド", "5", "調味料・食品", "860", "https://www.amazon.co.jp/%E3%83%97%E3%83%AC%E3%83%9F%E3%82%A2%E3%83%A0-%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%A0%E3%83%81%E3%83%BC%E3%82%BA-%E3%80%90%E3%82%A2%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%89%E3%80%91-OLIVE-ISLAND/dp/B081J6KFVY?th=1"],
            ["10", "さぬき骨付きどり（さぬき鳥本舗）", "6", "骨付きどり", "2260", "https://sanukihonetsukidori.co.jp/honetsuki-dori"],
            ["11", "食べるオリーブオイル（小豆島庄八）", "5", "調味料・食品", "960", "https://www.seto-s.com/shopdetail/000000000035/"],
            ["12", "丸島醬油ミニボトルシリーズ", "5", "調味料・食品", "1456", "https://marusima.shop-pro.jp/?mode=cate&cbid=848237&csid=1"],
            ["13", "純粋讃岐うどん・二人前つゆ付（うどん本陣山田家）", "3", "麵類", "1080", "https://www.ritsurinan.jp/shop/products/details/336"],
            ["14", "おととせんべい（象屋元蔵）", "2", "和菓子", "1500", "https://www.ototosenbei.com/order/"],
            ["15", "名物かまど", "2", "和菓子", "900", "https://kamado.jp/products/%E3%81%8B%E3%81%BE%E3%81%A9%E3%83%91%E3%82%A44"],
            ["16", "だしの素ゆたかあじ（堺屋醬油）", "5", "調味料・食品", "680", "http://www.sakaiya-soy.com/?pid=27405102"],
            ["17", "瀬戸内ショコラおれんじ（きさらぎ）", "1", "焼き菓子", "250", "http://www.kisaragi.co.jp/product/chocolat_orange.html"],
            ["18", "瓦せんべい（宗家くつわ堂）", "2", "和菓子", "702", "https://shop.kawarasenbei.jp/products/list?category_id=11"],
            ["19", "木守（三友堂）", "2", "和菓子", "1458", "https://store.shopping.yahoo.co.jp/kataharamachi/bbb0cda7c6.html"],
            ["20", "オリーブレモンカード（東洋オリーブ）", "5", "調味料・食品", "600", "https://www.tolea.jp/SHOP/F-5507.html"],
            ["21", "おいり（マイギフトカガワ）", "2", "和菓子", "1080", "https://mammygift.thebase.in/items/29249214"],
            ["22", "灸まん", "2", "和菓子", "600", "https://kyuman.co.jp/shop/products/list.php?category_id=2"],
            ["23", "手延べ半生オリーヴそうめん（創麵屋）", "3", "麵類", "432", "https://www.ritsurinan.jp/shop/products/details/1299"],
            ["24", "しょうゆ豆（大西食品）", "5", "調味料・食品", "1100", "https://www.onisi.co.jp/shopping/product_list.php"],
            ["25", "ふふふ。。吟醸酒300ml（MORIKUNI）", "4", "飲み物", "817", "https://www.morikuni.jp/?pid=58166416"],
            ["26", "オリーブサイダー", "4", "飲み物", "200", "https://www.1st-olive.com/SHOP/4580237117031.html"],
            ["27", "そうめんポリポリ（菊水堂）", "3", "麵類", "430", "https://www.camatoco.com/c-item-detail?ic=A000000047"],
            ["28", "エキストラバージンオリーブオイル（川本植物園）", "5", "調味料・食品", ", "],
            ["29", "島のパスタソース（小豆島庄八）", "5", "調味料・食品", "700", "https://www.seto-s.com/shopbrand/pasta-sauce/"],
            ["30", "小豆島産100%エキストラバージンオリーブオイル91g（100ml）（アグリオリーブオイル）", "5", "調味料・食品", "1080", "https://agri-olive.co.jp/?mode=cate&cbid=2796629&csid=0"],
            ["31", "オリーブ茶ペットボトル（ヤマヒサ）", "4", "飲み物", "162", "https://yama-hisa.jp/SHOP/9-1-1.html"]]