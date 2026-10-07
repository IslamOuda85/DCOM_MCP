"""Real stdio handshake and tool calls through the installed MCP SDK."""
import asyncio,json,os,sys
from pathlib import Path
from mcp import ClientSession,StdioServerParameters
from mcp.client.stdio import stdio_client

def test_stdio_protocol():
    async def run():
        root=Path(__file__).resolve().parents[1]
        env=dict(os.environ,COURSE_ROOT=str(root),PYTHONPATH=str(root))
        params=StdioServerParameters(command=sys.executable,args=['-m','dcom_mcp.server'],env=env)
        async with stdio_client(params) as (read,write):
            async with ClientSession(read,write) as session:
                await session.initialize()
                names={t.name for t in (await session.list_tools()).tools}
                assert {'search','fetch','get_asset','list_questions','get_teaching_context'}.issubset(names)
                result=await session.call_tool('search_course',{'query':'mesh topology','chapter':1})
                assert not result.isError and 'mesh' in result.content[0].text.lower()
                result=await session.call_tool('get_asset',{'asset_id':'ch01_ill_007'})
                assert not result.isError
                assert any(c.type=='image' for c in result.content)
                result=await session.call_tool('get_question',{'question_id':'P1-6'})
                assert not result.isError and 'ch01_ill_007' in result.content[0].text
                result=await session.call_tool('get_section',{'section_id':'../../etc/passwd'})
                assert result.isError
                assert (await session.list_prompts()).prompts
    asyncio.run(run())
