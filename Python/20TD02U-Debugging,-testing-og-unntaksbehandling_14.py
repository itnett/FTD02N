python
   import pytest
   import asyncio

   async def fetch_data():
       await asyncio.sleep(1)
       return "data"

   @pytest.mark.asyncio
   async def test_fetch_data():
       result = await fetch_data()
       assert result == "data"