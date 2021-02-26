from aiohttp import web


async def hello(request):
    return web.Response(text="Hello World")


async def manas(request):
    return web.Response(text="Hello Manas")


async def any_name(request):
    name = request.match_info.get('name', None)
    return web.Response(text="Hello {0}".format(name))


class EmployeeDetails(web.View):

    async def get(self):
        return web.json_response({"message": "Hello Employee"})

    async def post(self):
        data = await self.request.post()
        return web.Response(text="Hello {0}".format(data['name']))

    async def put(self, instance_id):
        print("HERE==================")
        data = await self.request.post()
        return web.Response(text="I am changing data for instance {0} to {1}".format(instance_id, data))


app = web.Application()
app.add_routes([web.get('/', hello)])
app.add_routes([web.get('/manas', manas)])
app.add_routes([web.get(r'/name/{name}', any_name)])
app.add_routes([web.view('/employee', EmployeeDetails)])
app.add_routes([web.view('/employee/{instance_id}', EmployeeDetails)])
web.run_app(app, host='127.0.0.1', port=8080)