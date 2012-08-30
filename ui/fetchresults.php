<?php

$isbn = $_GET['isbn'];
print $isbn;
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL,"http://localhost:6800/schedule.json");
curl_setopt($ch,CURLOPT_RETURNTRANSFER,1);
curl_setopt($ch, CURLOPT_POSTFIELDS,"project=scrapBib&spider=flipkartspider&isbn=$isbn");
$op1=json_decode(curl_exec($ch));
if($op1->status == "ok")
  print("ok");
curl_close ($ch);

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL,"http://localhost:6800/schedule.json");
curl_setopt($ch,CURLOPT_RETURNTRANSFER,1);
curl_setopt($ch, CURLOPT_POSTFIELDS,"project=scrapBib&spider=infibeamspider&isbn=$isbn");
$op2=json_decode(curl_exec($ch));
curl_close ($ch); 

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL,"http://localhost:6800/schedule.json");
curl_setopt($ch,CURLOPT_RETURNTRANSFER,1);
curl_setopt($ch, CURLOPT_POSTFIELDS,"project=scrapBib&spider=homeshopspider&isbn=$isbn");
$op3=json_decode(curl_exec($ch));
curl_close ($ch); 

?>

