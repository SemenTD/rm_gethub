from API.base import BaseAPI


class WaifuApi(BaseAPI):
    async def get_waifu(self, category: str, nsfv=False):

        if nsfv:
            waifu_type = "nsfw"
        else:
            waifu_type = "sfw"

        answer = await self.get(f'url/{waifu_type}/{category}')
        return answer['url']


waifu_api = WaifuApi()
