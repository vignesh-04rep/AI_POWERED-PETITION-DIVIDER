<?php
include("dbconnect.php");
session_start();
extract($_POST);
$date =date("Y-m-d");
date_default_timezone_set("Asia/Calcutta");
$time=date('g:i a');
$t=date('g:i', strtotime("now"));
if(isset($_POST['btn']))
{
$qry=mysql_query("select * from admin where uname='$uname' && password='$password'");
$num=mysql_num_rows($qry);
if($num==1)
{
$row=mysql_fetch_array($qry);
$uid=$row['id'];
$_SESSION['uid']=$uid;
?>
<script language="javascript">
alert("Login Successfully..");
//alert("Your Account Not Approval..");
window.location.href="adminhome.php";
</script>
<?php

}
else
{
?>
<script language="javascript">
alert("Login Unsuccessfully..");
//alert("Your Account Not Approval..");
window.location.href="login.php";
</script>
<?php
}
}
?>
<!DOCTYPE html>
<!--
Template Name: Abele
Author: <a href="https://www.os-templates.com/">OS Templates</a>
Author URI: https://www.os-templates.com/
Licence: Free to use under our free template licence terms
Licence URI: https://www.os-templates.com/template-terms
-->
<html>
<head>
<title>cloud user</title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<link href="layout/styles/layout.css" rel="stylesheet" type="text/css" media="all">
<style type="text/css">
<!--
.style1 {
	font-family: "Times New Roman", Times, serif;
	font-size: 24px;
	color: #22ACDD;
}
.style8 {font-family: "Times New Roman", Times, serif; font-size: 18px; }
-->
</style>
</head>
<body id="top">
<!-- ################################################################################################ -->
<!-- ################################################################################################ -->
<!-- ################################################################################################ -->
<div class="wrapper row0">
  <div id="topbar" class="clear"> 
    <!-- ################################################################################################ -->
    
    <div class="fl_right">
      <ul class="nospace linklist">
       
      </ul>
    </div>
    <!-- ################################################################################################ -->
  </div>
</div>
<!-- ################################################################################################ -->
<!-- ################################################################################################ -->
<!-- ################################################################################################ -->
<div class="wrapper row1">
  <header id="header" class="clear"> 
    <!-- ################################################################################################ -->
    <div id="logo" class="fl_left">
      <h1><a href="l"> </a></h1>
    </div>
    <!-- ################################################################################################ -->
    <nav id="mainav" class="fl_right"></nav>
    <!-- ################################################################################################ -->
  </header>
</div>
<!-- ################################################################################################ -->
<!-- ################################################################################################ -->
<!-- ################################################################################################ -->
<div class="wrapper row2 bgded" style="background-image:url('images/demo/backgrounds/1.jpg');">
  <div class="overlay">
    <div id="breadcrumb" class="clear"> 
      <!-- ################################################################################################ -->
      <ul>
        <li><a href="#">Login</a></li>
        <li><a href="#"> </a></li>
        <li></li>
        <li></li>
      </ul>
      <!-- ################################################################################################ -->
    </div>
  </div>
</div>
<!-- ################################################################################################ -->
<!-- ################################################################################################ -->
<!-- ################################################################################################ -->
<div class="wrapper row3">
  <main class="container clear"> 
    <!-- main body -->
    <!-- ################################################################################################ -->
    <div class="content"> 
      <!-- ################################################################################################ -->
      <h1> Welcome to cloud admin Login </h1>
      <p>&nbsp;</p>
      <div class="scrollable">
        <form name="form1" method="post" action="">
          <table width="100%" border="0" align="center">
            <tr>
              <td width="4%" rowspan="9">&nbsp;</td>
              <td width="38%" rowspan="9"><img width="300" height="425"><img src="images/admin.gif" width="300" height="270"></td>
              <td width="0%">&nbsp;</td>
              <td colspan="3"><div align="center" class="style1">Admin Login </div></td>
              <td width="34%">&nbsp;</td>
            </tr>
            <tr>
              <td>&nbsp;</td>
              <td width="9%">&nbsp;</td>
              <td colspan="2">&nbsp;</td>
              <td>&nbsp;</td>
            </tr>
            <tr>
              <td height="38">&nbsp;</td>
              <td><span class="style8">User Name </span></td>
              <td colspan="2">
                <input name="uname" type="text" id="uname" required="">
              </td>
              <td>&nbsp;</td>
            </tr>
            <tr>
              <td height="35">&nbsp;</td>
              <td><span class="style8">Password</span></td>
              <td colspan="2">
                <input name="password" type="password" id="password" required="">
             </td>
              <td>&nbsp;</td>
            </tr>
            <tr>
              <td>&nbsp;</td>
              <td>&nbsp;</td>
              <td colspan="2">&nbsp;</td>
              <td>&nbsp;</td>
            </tr>
            <tr>
              <td>&nbsp;</td>
              <td>&nbsp;</td>
              <td width="7%">
                <input name="btn" type="submit" id="btn" value="Submit">
              </td>
              <td width="8%"><input type="reset" name="Submit2" value="Reset"></td>
              <td>&nbsp;</td>
            </tr>
            <tr>
              <td>&nbsp;</td>
              <td>&nbsp;</td>
              <td colspan="2">&nbsp;</td>
              <td>&nbsp;</td>
            </tr>
            <tr>
              <td>&nbsp;</td>
              <td>&nbsp;</td>
              <td colspan="2">&nbsp;</td>
              <td>&nbsp;</td>
            </tr>
            <tr>
              <td>&nbsp;</td>
              <td>&nbsp;</td>
              <td colspan="2">&nbsp;</td>
              <td>&nbsp;</td>
            </tr>
          </table>
        </form>
      </div>
      <!-- ################################################################################################ -->
    </div>
    <!-- ################################################################################################ -->
    <!-- / main body -->
    <div class="clear"></div>
  </main>
</div>
<!-- ################################################################################################ -->
<!-- ################################################################################################ -->
<!-- ################################################################################################ -->
<div class="wrapper row4">
  <section id="cta" class="clear"> 
    <!-- ################################################################################################ --><!-- ################################################################################################ -->
</section>
</div>
<!-- ################################################################################################ -->
<!-- ################################################################################################ -->
<!-- ################################################################################################ -->
<div class="wrapper row5">
  <footer id="footer" class="clear"> 
    <!-- ################################################################################################ -->
    <!-- ################################################################################################ -->
</footer>
</div>
<!-- ################################################################################################ -->
<!-- ################################################################################################ -->
<!-- ################################################################################################ -->
<div class="wrapper row6">
  <div id="copyright" class="clear"> 
    <!-- ################################################################################################ -->
    <p class="fl_left">Copyright &copy; 2018 - All Rights Reserved - <a href="#">Domain Name</a></p>
    <p class="fl_right">Template by <a target="_blank" href="https://www.os-templates.com/" title="Free Website Templates">OS Templates</a></p>
    <!-- ################################################################################################ -->
  </div>
</div>
<!-- JAVASCRIPTS -->
<script src="../layout/scripts/jquery.min.js"></script> 
<script src="../layout/scripts/jquery.mobilemenu.js"></script>
</body>
</html>