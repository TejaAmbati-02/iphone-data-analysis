from ast import main
import asyncio

class Coroutine:


    # async def fetch_data(self, delay):
    #     print("Fetching data....")
    #     await asyncio.sleep(delay)
    #     print("Data fetched")
    #     return {'data':'Sone data'}

    #Coroutine Function
    # async def main(self):
    #     print("Start of main coroutine")
    #     task = self.fetch_data(2)

    #     print("End of main coroutine")

    #     result = await task
    #     print(f"Received result : {result}")


    # async def fetch_data(self, delay, id):
    #     print("Fetching data.... id : ", id)
    #     await asyncio.sleep(delay)
    #     print("Data fetched, id : ", id)
    #     return {'data':'Some data', 'id': id}


    # async def main(self):
    #     task1 = self.fetch_data(2, 1)
    #     task2 = self.fetch_data(2, 2)

    #     result1 = await task1
    #     print(f"Received result: {result1}")
        
    #     result2 = await task2
    #     print(f"Received result: {result2}")




    async def fetch_data(self, id, sleep_time):
        print(f"Coroutine {id} starting to fetch data.")
        await asyncio.sleep(sleep_time)
        return {"id":id, "data":f"Sample data from coroutine {id}"}



    async def main(self):

        task1 = asyncio.create_task(self.fetch_data(1,2))
        task2 = asyncio.create_task(self.fetch_data(2,3))
        task3 = asyncio.create_task(self.fetch_data(3,2))

        result1 = await task1
        result2 = await task2
        result3 = await task3


        print(result1, result2, result3)








coroutine = Coroutine()
#Run main coroutine
# main() -> Return Coroutine Object
asyncio.run(coroutine.main())

