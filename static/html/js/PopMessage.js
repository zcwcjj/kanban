/*
*描    述：用于提醒弹出框的展示
*          1. 调用show方法前先创建PopMessage实例
*          2. show(jsonContents)方法接收json对象参数，对象格式示例：[{"description":"描述1","href":"http://www.baidu.com"},{"description":"描述2","href":"http://www.baidu.com"}]
*/
var rootPath = getRootPath(); // 获得网站根路径
//var showFrame;

var PopMessage = function () {
    //    var opt = this.setOptions(options);
    //    this.showInterval = opt.showInterval;
    //    this.showFrame = opt.showFrame;

    this.oncreate();
};

// 创建提示窗体
PopMessage.prototype = {
    // 设置项
    //    setOptions: function (options) {
    //        this.options = {
    //            showInterval: 6000, //默认值
    //            showFrame: window.location   // 要显示的位置
    //        };
    //        return this.options;
    //    },
    oncreate: function () {
        
        // 设置样式
        var wrapperStyle = "margin: 0px;padding: 0px;font-size: 14px;";
        var tipStyle = "position: absolute;right: 5px;bottom: -5px;height: 0px;overflow: hidden;display: none;z-index: 0;";
        
        // 设置html
        var popHtml = "<div id='popMessage' style='" + wrapperStyle + "'>";
        popHtml += "<div id='popMessage-tip' style='" + tipStyle + "'>";
        popHtml += "<table width='300px' cellpadding='0' cellspacing='0'>";

        // title 标题栏
        popHtml += "<tr style='height:25px'>";
        popHtml += "<td style='width:10px;background:url(" + rootPath + "/Common/PopMessage/images/window_01.png) no-repeat 0 0'></td>";
        popHtml += "<td style='color:white;width:280px;background:url(" + rootPath + "/Common/PopMessage/images/window_02.png) repeat-x 0 0'><img style='cursor:pointer; margin-top:3px;float: right;' alt='关闭提醒' title='关闭提醒' src='" + rootPath + "/Common/PopMessage/images/close.png' onclick='javascript:downPopMessage()' />新消息</td>";
        popHtml += "<td style='width:10px;background:url(" + rootPath + "/Common/PopMessage/images/window_03.png) no-repeat 0 0'></td>";
        popHtml += "</tr><tr style='height:150px'>";

        // 内容
        popHtml += "<td style='background:url(" + rootPath + "/Common/PopMessage/images/window_04.png) repeat-y 0 0'></td>";
        popHtml += "<td style='background:url(" + rootPath + "/Common/PopMessage/images/window_05.png) repeat 0 0'>";
        // 提醒内容
        popHtml += "<ul id='popMessage-contents' style='text-align:center;line-height:25px;font-size:12px;list-style:none;cursor:pointer'></ul></td>";
        popHtml += "<td style='background:url(" + rootPath + "/Common/PopMessage/images/window_06.png) repeat-y 0 0'></td></tr></table>";

        popHtml += "</div></div>";

        document.body.innerHTML += popHtml;
        return this.options;
        
    },

    show: function () {
        //showInterval = interval;
        ////showFrame = locationFrame;
        /*
        // 绑定鼠标悬停面板和离开事件
        $("#popMessage-tip").mouseenter(function () {
            clearInterval(showTimer);
            showTimer = -1;
        }).mouseleave(function () {
            downPopMessage();
        });
        */
        //getData();
        //showTimer = setInterval("getData();", showInterval);
    }
}
//var showTimer;

function keepAlive(obj) {
}

/*
function redirect() {
    var location = document.getElementById(showFrame).getBoundingClientRect();
    var width = location.right - location.left;
    var height = location.bottom - location.top;
    var left = (width - 200) / 2 + location.left + "px";
    var top = (height - 50) / 2 + location.top + "px";

    var aHtml = "<table id='popMessage-redirect' width='200px' style='background:white;position: absolute;left:" + left + ";top:" + top + ";border:1px solid #007ea2'>";
    aHtml += "<tr style='height:50px'>";
    aHtml += "<td style='text-align:right;width:80px'><img src='" + rootPath + "/Common/PopMessage/images/loading.gif' /></td>";
    aHtml += "<td style='width:120px'>正在跳转...</td></tr></table>";

    document.body.innerHTML += aHtml;
}
*/

/*
function loadpage(href) {
    document.getElementById(showFrame).src = href;
}
*/
function downPopMessage() {
    /*
    if (showTimer == -1) {
        showPopMessage();
        showTimer = setInterval("getData();", showInterval);
    }
    */
}

function getData() {
    $.get(rootPath + "/Common/PopMessage/PopMessageHandler.ashx?" + new Date(),
        function (data, status) {
            bindContents(data);
        });
    }
   
// 解析json对象并绑定到提示框中
    function bindContents(jsonContents) {

    // 1. 检查有无提醒信息，若无提醒则返回
    if (jsonContents == "") return;

    // 2. 绑定提醒信息
    var result = eval("(" + jsonContents + ")");
    var aHtml = "";
    for (var i = 0; i < result.length; i++) {
        /*
        var currentSrc = window.frames[showFrame].location.href;
        if (currentSrc != undefined) {
            var currentpaths = currentSrc.split("/");
            var resultspaths = result[i].href.split("/");
            var currentpage = currentpaths[currentpaths.length - 1].split("?");
            var resultspage = resultspaths[resultspaths.length - 1].split("?");

            if (1== 1) //原currentpage[0] != resultspage[0] 改为1=1弹窗;待办提示3种待办,当办理其中一种时,也弹窗是为了提示其它待办
            {
            */
                var ids = result[i].ids.split(',');
                var desList = result[i].description.split(','); //描述：支持多条
                //var numList = result[i].count.split('-'); //数量：支持多条
                //var linkList = result[i].href.split('-'); //链接：支持多条
                var numList = result[i].count; //数量
                var linkurl = result[i].href; //链接
                var nexttimes = result[i].nexttimes.split(',');

                for (var j = 0; j < desList.length; j++) {
                    linkList = linkurl + ids[j];
                    aHtml += "<li> <a style='color:#436EEE;' onclick='javascript:loadpage(\"" + linkList + "\");'>" + desList[j] + "<span style='color:red;font-weight:bolder'>下次维保时间:" + nexttimes[j] + "</span>" + "</a></li>";
                }

                aHtml += "<li><span>点击以上链接查看处理</span></li>";
                
            //}
        //}
    }

   if (aHtml != "") {
        document.getElementById("popMessage-contents").innerHTML = aHtml;

        // 3. 显示提醒消息
        showPopMessage();
    }   
}

// 显示提醒消息
var handle;
function showPopMessage() {
    var obj = document.getElementById("popMessage-tip");
    if (parseInt(obj.style.height) == 0) {
        obj.style.display = "block";
        handle = setInterval("changeH('up')", 2);
    } else {
        handle = setInterval("changeH('down')", 2);
    }
}

// 改变提醒框高度
function changeH(str) {
    var obj = document.getElementById("popMessage-tip");
    if (str == "up") {
        if (parseInt(obj.style.height) > 175)
            clearInterval(handle);
        else
            obj.style.height = (parseInt(obj.style.height) + 8).toString() + "px";
    }
    if (str == "down") {
        if (parseInt(obj.style.height) < 8) {
            clearInterval(handle);
            obj.style.display = "none";
        }
        else
            obj.style.height = (parseInt(obj.style.height) - 8).toString() + "px";
    }
}

//js获取项目根路径，如： http://localhost:8083/uimcardprj
function getRootPath() {
    //获取当前网址，如： http://localhost:8083/uimcardprj/share/meun.jsp    
    var curWwwPath = window.document.location.href;
    //获取主机地址之后的目录，如： uimcardprj/share/meun.jsp    
    var pathName = window.document.location.pathname;
    var pos = curWwwPath.indexOf(pathName);
    //获取主机地址，如： http://localhost:8083    
    var localhostPaht = curWwwPath.substring(0, pos);
    //获取带"/"的项目名，如：/uimcardprj    
    var projectName = pathName.substring(0, pathName.substr(1).indexOf('/') + 1);

    if (projectName == "/Frame") {
        projectName = "";
    }
    return (localhostPaht + projectName);
}
