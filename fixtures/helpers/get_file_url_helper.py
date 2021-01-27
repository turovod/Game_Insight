class GetFileUrl:

    def get_file_url(self, local_url):
        wd_url = __file__.strip('fixtures\get_file_url_helper.py')
        wd_url = "".join([wd_url, local_url])
        return wd_url
