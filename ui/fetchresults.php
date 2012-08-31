<?php
$result = "";
$isbn = $_GET['isbn'];
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL,"http://localhost:6800/schedule.json");
curl_setopt($ch,CURLOPT_RETURNTRANSFER,1);
curl_setopt($ch, CURLOPT_POSTFIELDS,"project=scrapBib&spider=flipkartspider&isbn=$isbn");
$op1=json_decode(curl_exec($ch));
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


sleep(5);
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL,"http://localhost:6800/listjobs.json");
curl_setopt($ch,CURLOPT_RETURNTRANSFER,1);
curl_setopt($ch, CURLOPT_POSTFIELDS,"project=scrapBib");
$op=json_decode(curl_exec($ch),true);
curl_close ($ch); 
while(empty($op["jobs"])==false)
{
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL,"http://localhost:6800/listjobs.json");
curl_setopt($ch,CURLOPT_RETURNTRANSFER,1);
curl_setopt($ch, CURLOPT_POSTFIELDS,"project=scrapBib");
$op=json_decode(curl_exec($ch),true);
curl_close ($ch); 
}
sleep(8);
$result = file_get_contents('results.out');

print $result;

file_put_contents("results.out","");
?>

