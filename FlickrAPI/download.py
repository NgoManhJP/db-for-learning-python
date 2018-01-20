from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint   #データを表示するため
from retry import retry
import os, time, sys, traceback    #OSの情報を得るため

# Flickr APIキーの情報
# https://www.flickr.com/services/apps/create/apply/
flickr_api_key = ""
secret_key = ""

keyword = sys.argv[1] #argument value パラメータの値

# 実際に実行してみるとたまに接続に失敗するので、失敗時にリトライするライブラリを使い
@retry()
def get_photos(url, filepath):
    urlretrieve(url, filepath)
    time.sleep(1)

if __name__ == '__main__':
    flickr = FlickrAPI(flickr_api_key, secret_key, format = 'parsed-json')
    result = flickr.photos.search(
        #検索パラメータに値を与える
        text = keyword,         #　検索キーワード (保存フォルダ名と同じにする)
        per_page = 40,          #　外れデータを除くので、多めに取得しておく
        media = 'photos',       #　検索データの種類　→　写真を指定する
        sort = 'relevance',     #　データのソート順：検索の関連順に並べる
        safe_search = 1,        #　有害コンテンツ表示しないオプション
        extras = 'url_q, licence' # 取得したいオプション値; url_q: 画像のアドレスが入っているデータ; ライセンス情報
    )
    photos = result['photos']

    try:
        if not os.path.exists('./image-data/' + keyword):
            os.mkdir('./image-data' + keyword)

        for photo in photos['photo']:
            url_q = photo['url_q']
            filepath = './image-data' + keyword + '/' + photo['id'] + '.jpg'
            get_photos(url_q, filepath)

    except Exception as e:
        traceback.print_exc()
