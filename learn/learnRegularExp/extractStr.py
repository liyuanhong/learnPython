#coding:utf-8

'''
使用正则表达式提取某些特定的字符串
'''
import re
str = '''
<title>设备管理系统</title>
<link href="http://wscdn.miaopai.com/static20131031/company/imgs/favicon.ico" rel="SHORTCUT ICON">
<script src="http://newdev.yixia.com/static/devMS/js/jquery-3.1.1.min.js"></script>
<script src="http://newdev.yixia.com/static/devMS/js/jquery.cookie.js"></script>
<link href="http://newdev.yixia.com/static/dist/css/bootstrap.min.css" rel="stylesheet">
<link href="http://newdev.yixia.com/static/devMS/css/index.css" rel="stylesheet">
<script src="http://newdev.yixia.com/static/devMS/js/index.js"></script>

<div id="main">
	<div id="top_bar">
		<label style="color:white;font-size:20px;margin-left:45px;margin-top:8px;">设备管理系统</label>
		<div>
			<label id="logout_lagel" class="login_label" onclick="logout()">退出</label><label style="font-size: 14px;padding-top: 10px;color: #31B0F4;margin-left: 0px;height: 100%;width: 110px;background-color: #1A4FA3;text-align: center;" >welcome~</label>		</div>
	</div>
	<div style="width: 100%;height:100%;">
		<div id="left_item">
			<div class="setting_item">
				<label id = "searchDevices" class="setting_label menu_selected" onclick="changeMenu(event)">设 备 查 询</label>
			</div>
			<div class="setting_item"><label id = "addDevices" class="setting_label" onclick="changeMenu(event)">添 加 设 备</label></div>			<div class="setting_item"><label id = "manDevices" class="setting_label" onclick="changeMenu(event)" >管 理 设 备</label></div>			<div class="setting_item"><label id = "checkDevices" class="setting_label" onclick="changeMenu(event)">设 备 盘 点</label></div>			<div class="setting_item"><label id = "logMan"class="setting_label" onclick="changeMenu(event)">日 志 管 理</label></div>			<div class="setting_item"><label id = "userMan" class="setting_label" onclick="changeMenu(event)">用 户 管 理</label></div>						<div class="setting_item">
				<label id = "myPage" class="setting_label " onclick="changeMenu(event)">我 的 页 面</label>
			</div>
			<div class="setting_item"><label id = "otherToolsPage" class="setting_label" onclick="changeMenu(event)">附 加 功 能</label></div>			<div class="setting_item">
				<label id = "aboutPage" class="setting_label " onclick="changeMenu(event)">关 于 系 统</label>
			</div>
		</div>
		<div id="right_content">
			
<link href="http://newdev.yixia.com/static/devMS/css/showDev/showDevs.css" rel="stylesheet">
<div id="search_area">
	<div>
		<table _border="1" style="width:100%;height:100px;margin-left:20px;">
			<tr>
				<td style="width:33%;">
					<label class="label_style">平台：</label>
					<select id="dev_plateform" class="select_style form-control">
						<option value="all">all</option>
						<option value="android">android</option>
						<option value="ios">ios</option>
					</select>
				</td>
				<td style="width:33%;">
					<label class="label_style">品牌：</label>
					<select id="dev_brand" class="select_style form-control">
						<option value="all">all</option>
						<option value="三星">三星</option>
						<option value="小米">小米</option>
						<option value="华为">华为</option>
						<option value="魅族">魅族</option>
						<option value="oppo">oppo</option>
						<option value="vivo">vivo</option>
						<option value="联想">联想</option>
						<option value="中兴">中兴</option>
						<option value="nexus">nexus</option>
						<option value="其他">其他</option>
					</select>
				</td>
				<td style="width:33%;">
					<label class="label_style">系统版本：</label>
					<select id="dev_version" class="select_style form-control">
						<option value="all">all</option>
						<option value="8">8</option>
						<option value="7">7</option>
						<option value="6">6</option>
						<option value="5.1">5.1</option>
						<option value="5.0">5.0</option>
						<option value="4.4">4.4</option>
						<option value="4.3">4.3</option>
						<option value="4.2">4.2</option>
						<option value="4.1">4.1</option>
						<option value="ios7">ios7</option>
						<option value="ios8">ios8</option>
						<option value="ios9">ios9</option>
						<option value="ios10">ios10</option>
					</select>
				</td>
			</tr>
			<tr>
				<td>
					<label class="label_style" class="label_style">状态：</label>
					<select id="dev_status" class="select_style form-control">
						<option value="all">all</option>
						<option value="2">已借出设备</option>
						<option value="0">未借出设备</option>
						<option value="1">申请中</option>
					</select>
				</td>
				<td>
					<label>分类：</label>
					<select id="dev_category"  class="select_style form-control" style="margin-left:0px;">
						<option value="all" >all</option>
						<option value="手机">手机</option>
						<option value="平板">平板</option>
						<option value="其他">其他</option>
					</select>
				</td>
				<td>
					<label>签借人：</label>
					<input id="borrower" class="form-control select_style" style="margin-left: 15px;"></input>
				</td>
			</tr>
		</table>
	</div>
	<div>
		<button class="btn btn-primary" style="width:100px;" id="search_btn" onclick="searchDevs()">查 询</button>
	</div>
	<div>
		<table class="table table-striped">
			<thead>
				<tr>
					<th>id</th>
					<th>icon</th>
					<th>设备名</th>
					<th>型号</th>
					<th>编号#</th>
					<th>签借人</th>
					<th>申请</th>
					<th style="color:red;">所属</th>
					<th>借出时间</th>
				</tr>
			</thead>
			<tbody>
			<tr><td>1</td><td><img onclick="showDevInfo()" class="dev_icon" id="icon_261"src="http://newdev.yixia.com/files/thumbnail/IMG_20171107_152800.jpg"></img></td><td id="label_261">华为畅享7</td><td>SLA-AL00</td><td>03-0245</td><td>王显鹏</td><td></td><td style="color:red;">李远洪</td>
					<td>2018-03-05 14:46</td>
					</tr><tr><td>2</td><td><img onclick="showDevInfo()" class="dev_icon" id="icon_204"src="http://newdev.yixia.com/files/thumbnail/IMG_20170909_113746.jpg"></img></td><td id="label_204">华为 2plus</td><td>BAC-AL00</td><td>03-0204</td><td>李甜</td><td></td><td style="color:red;">李甜</td>
					<td>2017-07-27 15:05</td>
					</tr><tr><td>3</td><td><img onclick="showDevInfo()" class="dev_icon" id="icon_203"src="http://newdev.yixia.com/files/thumbnail/IMG_20170829_173540.jpg"></img></td><td id="label_203">华为荣耀V9</td><td>Honor V9</td><td>03-0203</td><td>汪蒙蒙</td><td></td><td style="color:red;">汪蒙蒙</td>
					<td>2017-11-20 20:25</td>
					</tr><tr><td>4</td><td><img onclick="showDevInfo()" class="dev_icon" id="icon_189"src="http://newdev.yixia.com/files/thumbnail/IMG_20170609_103847.jpg"></img></td><td id="label_189">华为荣耀V9</td><td>Honor V9</td><td>03-0187</td><td>孙都</td><td></td><td style="color:red;">李远洪</td>
					<td>2018-02-07 14:24</td>
					</tr><tr><td>5</td><td><img onclick="showDevInfo()" class="dev_icon" id="icon_180"src="http://newdev.yixia.com/files/thumbnail/"></img></td><td id="label_180">华为P10</td><td>P10</td><td>03-0170</td><td>徐艳习</td><td></td><td style="color:red;">朱慧敏</td>
					<td>2017-11-16 13:49</td>
					</tr><tr><td>6</td><td><img onclick="showDevInfo()" class="dev_icon" id="icon_173"src="http://newdev.yixia.com/files/thumbnail/HW6X.jpeg"></img></td><td id="label_173">华为畅玩6x</td><td>Honor 6X</td><td>03-0159</td><td>井琳</td><td></td><td style="color:red;">孟墨</td>
					<td>2017-10-26 15:17</td>
					</tr><tr><td>7</td><td><img onclick="showDevInfo()" class="dev_icon" id="icon_165"src="http://newdev.yixia.com/files/thumbnail/HWP10.jpeg"></img></td><td id="label_165">华为P10</td><td>VTR-TL00</td><td>03-0160</td><td>汪莉丽</td><td></td><td style="color:red;">孟墨</td>
					<td>2017-10-26 15:18</td>
					</tr><tr><td>8</td><td><img onclick="showDevInfo()" class="dev_icon" id="icon_160"src="http://newdev.yixia.com/files/thumbnail/IMG_20170304_115516.jpg"></img></td><td id="label_160">华为mate9</td><td>MHA-AL00</td><td>03-0146</td><td>罗志华</td><td></td><td style="color:red;">汪蒙蒙</td>
					<td>2017-11-20 20:26</td>
					</tr><tr><td>9</td><td><img onclick="showDevInfo()" class="dev_icon" id="icon_159"src="http://newdev.yixia.com/files/thumbnail/IMG_20170220_184249.jpg"></img></td><td id="label_159">华为P9</td><td>EVA-AL00</td><td>03-0141</td><td><input type="text" class="form-control" style="width:80px;" id="input_159"></td><td><button class="btn btn-sm btn-success" onclick="applyFor()" id="159">申 请</button></td><td style="color:red;">李远洪</td>
					<td></td>
					</tr><tr><td>10</td><td><img onclick="showDevInfo()" class="dev_icon" id="icon_156"src="http://newdev.yixia.com/files/thumbnail/IMG_20170214_170823.jpg"></img></td><td id="label_156">华为mate9</td><td>MHA-AL00</td><td>03-0133</td><td><input type="text" class="form-control" style="width:80px;" id="input_156"></td><td><button class="btn btn-sm btn-success" onclick="applyFor()" id="156">申 请</button></td><td style="color:red;">王晶磊</td>
					<td></td>
					</tr>				
			</tbody>
		</table>
	</div>
</div>
		</div>
	</div>
</div>
'''

#提取姓名
findStr = re.findall(u';">(.+)</td',str)
print "文中的姓名如下："
for tem in findStr:
    print tem

#提取url
findStr = re.findall(u'"(http://[^"]+)"',str)
print "文中的url如下(方法一)："
for tem in findStr:
    print tem

'''
提取url（使用？符号来作非为贪婪匹配）：
1、什么是正则表达式的贪婪与非贪婪匹配

　　如：String str="abcaxc";

　　　　Patter p="ab*c";

　　贪婪匹配：正则表达式一般趋向于最大长度匹配，也就是所谓的贪婪匹配。如上面使用模式p匹配字符串str，结果就是匹配到：abcaxc(ab*c)。

　　非贪婪匹配：就是匹配到结果就好，就少的匹配字符。如上面使用模式p匹配字符串str，结果就是匹配到：abc(ab*c)。
2、编程中如何区分两种模式

　　默认是贪婪模式；在量词后面直接加上一个问号？就是非贪婪模式。

　　下面的都是量词：

                    {m,n}：m到n个

　　　　　*：任意多个

　　　　　+：一个到多个

　　　　　？：0或一个
'''
findStr = re.findall(u'"(http://.+?)"',str)
print "文中的url如下(方法二)："
for tem in findStr:
    print tem