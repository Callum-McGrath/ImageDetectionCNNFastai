# %%
def search_images(term, max_images=30):
    from duckduckgo_search import ddg_images
    return L(ddg_images(term, max_results=max_images)).itemgot('image')

# %%
def ImageDownloader(SearchPhrase,DestinationFolder,max_images=10,):
    urls=search_images(SearchPhrase, max_images)
    import os
    import requests
    dest=DestinationFolder+str(SearchPhrase.replace(' ',''))
    if os.path.exists(dest)==False:
        os.makedirs(dest)
    for i in urls:
        try:
            print(urls.index(i))
            data=requests.get(i).content
            filename=SearchPhrase.replace(' ', '')+str(urls.index(i))+'.jpg'
            with open(f'{dest}/{filename}','wb') as handler:
                handler.write(data)
        except:
            print(urls.index(i)+' was unsuccessful')
    print('Download Complete')


# %%
def ImageIntegrityVerifier(DestinationFolder):
    import os
    from PIL import Image
    photos=os.listdir(DestinationFolder)
    for i in photos:
        try:
            Image.open(DestinationFolder+'\\'+str(i),'r')
        except:
            os.unlink(DestinationFolder+'\\'+str(i))
            print(f'file {i} was removed')
