from rest_framework.renderers import JSONRenderer


class CustomRenderer(JSONRenderer):
    # 重构render方法
    def render(self, data, accepted_media_type=None, renderer_context=None):
        code = 0
        if renderer_context:
            if isinstance(data, dict):
                msg = data.pop('msg', 'success')
                code = data.pop('code', 0)
            else:
                msg = 'success'
            # 重新构建返回的JSON字典

            ret = {
                'msg': msg,
                'code': code,
                'data': data,
            }
            # 返回JSON数据
            return super().render(ret, accepted_media_type, renderer_context)
        else:
            return super().render(data, accepted_media_type, renderer_context)
