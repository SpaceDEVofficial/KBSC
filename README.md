# Koreanbots-Bot-Servers-Chart
[fsanchir](<https://github.com/fsanchir/Koreanbots-Bot-Servers-Chart>)님의 레퍼를 포크해 현재 'Konosuba'봇에 사용되고있는 소스로 변경한 레포입니다.

## 사용법
- config.py 파일의 bot_id에서, 본인의 봇 아이디를 " "안에 기입해주세요.
- korbots_server_collector.py를 켜시고, korbots_statistics_web_server.py를 켜 주세요.
- [db파일](<https://github.com/SpaceDEVofficial/KBSC/blob/main/server/db/db.db>)은 따로 만지실 필요가 없습니다. 최초 구동시 자동으로 테이블을 구성합니다.
 
서버차트: http://localhost:5000/get?type=image
 
투표차트: http://localhost:5000/voteget?type=image

[korbots_statistics_web_server.py](<https://github.com/SpaceDEVofficial/KBSC/blob/446608672e06abbb61214fe8a4eb5761adece18c/korbots_statistics_web_server.py#L20>)에 20번째줄에 있는 코드는

자동으로 데이터 값을 잘라내어 텍스트가 겹치지않게 해줍니다.
```python
# 자동 데이터값 컷팅
if len(data) > 47:
    data = data[(len(data) - 47):]
```
## Example Image

서버수 차트
![서버차트](<https://media.discordapp.net/attachments/884407186854404106/888801756362977280/output.png?width=1056&height=549>)

투표수 차트
![투표차트](<https://media.discordapp.net/attachments/884407186854404106/888790778770497566/output.png?width=1056&height=549>)
# 라이센스
이 레포는 MIT 라이센스를 따릅니다. 따라, 봇의 도움말, 레포 오픈소스 알림 등에 출처를 기제해주세요.
