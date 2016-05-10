$(document).ready(function () {
    // Store variables
    var accordion_head = $('.accordion > li > a'), accordion_body = $('.accordion li > .sub-menu');
    // Open the first tab on load
    accordion_head.first().addClass('active').next().slideDown(
			'normal');
    // Click function
    accordion_head.on('click', function (event) {
        // Disable header links
        event.preventDefault();
        // Show and hide the tabs on click
        if (!$(this).hasClass('active')) {
            accordion_body.slideUp('normal');
            $(this).next().stop(true, true).slideToggle(
						'normal');
            accordion_head.removeClass('active');
            $(this).addClass('active');
        }
        else {
            accordion_body.slideUp('normal');
            accordion_head.removeClass('active');
        }
    });
    var curWindowUrl = window.location.href;
    if (curWindowUrl.indexOf("redirectUrl") > 0) {
        var pos = curWindowUrl.indexOf("redirectUrl=");
        var length = "redirectUrl=".length
        var redirectUrl = curWindowUrl.substring(pos + length);
        openUrl(redirectUrl, false, "");
    }
  
    window.setInterval(getDate, 1000);  //每隔一秒显示时间
});

//打开功能页面
function openUrl(url,isMain,title) {
	if(isMain){
		$(".Backstage-top .sp3").hide();
		$(".Backstage-top .sp3").next("a").hide();
	}
	else{
		$(".Backstage-top .sp3").show();
		$(".Backstage-top .sp3").next("a").attr("title",title);
		$(".Backstage-top .sp3").next("a").text(title);
		$(".Backstage-top .sp3").next("a").show();
	}
	$("#ifr").attr("src",url);
}

function getDate(){
    var date=new Date();
    
    var year=date.getFullYear();  //年
    var syear=year+"年";
    
   var month=date.getMonth()+1;  //月
   var smonth = month+"月";
   
   var da=date.getDate(); //日
   var sda=da+"日"; 
   
   var currentArray=new Array('星期日','星期一','星期二','星期三','星期四','星期五','星期六');
   var week = currentArray[date.getDay()];
   
   var hour=date.getHours(); //时间
   if(hour>12){
	   hour='下午'+(hour-12);
   }
   else{
	   hour='上午'+hour;
   }
   
   var minutes=date.getMinutes(); //分钟 
   if(minutes.toString().length==1)
	   minutes="0"+minutes;

   var second=date.getSeconds(); //秒
   if(second.toString().length==1)
	   second="0"+second;
   
   $('#li_time').text(syear+','+smonth+sda+','+week+','+hour+':'+minutes+':'+second);
}



/**
 * 收缩、展开侧边栏
 * @return
 */
function toggleLeft(){
	if($('.Backstage-side').children('div').is(':hidden')){
		$('.Backstage-side').children('div').show();
		$('.Backstage-side').animate({width:"216px"},function(){
			$('#img_leftBtn').attr('src','images/v2.jpg');
		});
	}
	else{
		shrinkLeft();
	}
}

/**
 * 收缩侧边栏
 * @return
 */
function shrinkLeft(){
	if($('.Backstage-side').children('div').is(':visible')){
		$('.Backstage-side').animate({width:"5px"},function(){
			$('.Backstage-side').children('div').hide();
			$('#img_leftBtn').attr('src','images/v1.jpg');
		});
	}
}

function changeType(type){
	if(type==1){
		$("#li2").removeClass();
		$("#li1").addClass("liOn");
		$("#loginPassword").show();
		$("#transPassword").hide();
	}else{
		$("#li2").addClass("liOn");
		$("#li1").removeClass();
		$("#transPassword").show();
		$("#loginPassword").hide();
	}
}



}