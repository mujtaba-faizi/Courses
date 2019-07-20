set ns [new Simulator]

$ns color 1 Red
$ns color 2 Blue

set nf [open out.nam w]
$ns namtrace-all $nf
set nd [open out.tr w]
set myFile1 [open out0.tr w]
set myFile2 [open out1.tr w]
$ns trace-all $nd


proc finish {} {
global ns nd nf myFile1 myFile2 
close $myFile1
close $myFile2
$ns flush-trace

close $nf
close $nd

exec nam out.nam &
exec xgraph out0.tr out1.tr -geometry 800x400 &
exit 0

}

set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]
set n4 [$ns node]
set n5 [$ns node]


$ns duplex-link $n0 $n2 10Mb 10ms DropTail
$ns duplex-link $n1 $n2 10Mb 10ms DropTail
$ns duplex-link $n2 $n3 5Mb 20ms SFQ
$ns duplex-link $n3 $n4 10Mb 10ms DropTail
$ns duplex-link $n3 $n5 10Mb 10ms DropTail


$ns duplex-link-op $n0 $n2 orient right-down
$ns duplex-link-op $n1 $n2 orient right-up
$ns duplex-link-op $n2 $n3 orient right
$ns duplex-link-op $n3 $n4 orient right-up
$ns duplex-link-op $n3 $n5 orient right-down


$ns duplex-link-op $n2 $n3 queuePos 0.5


set udp0 [new Agent/UDP]
$ns attach-agent $n1 $udp0
$udp0 set fid_ 1


set cbr0 [new Application/Traffic/CBR]
$cbr0 set packetSize_ 500
$cbr0 set rate_ 5mb
$cbr0 attach-agent $udp0




set tcp [new Agent/TCP]
$ns attach-agent $n0 $tcp
$tcp set fid_ 2

set sink [new Agent/TCPSink]
$ns attach-agent $n4 $sink
$ns connect $tcp $sink


set ftp0 [new Application/FTP]
$ftp0 attach-agent $tcp
$ftp0 set type_ FTP


set tcp1 [new Agent/TCP]
$ns attach-agent $n0 $tcp1
$tcp1 set fid_ 2

set sink [new Agent/TCPSink]
$ns attach-agent $n4 $sink
$ns connect $tcp1 $sink


set ftp1 [new Application/FTP]
$ftp1 attach-agent $tcp1
$ftp1 set type_ FTP

set tcp2 [new Agent/TCP]
$ns attach-agent $n0 $tcp2
$tcp2 set fid_ 2

set sink [new Agent/TCPSink]
$ns attach-agent $n4 $sink
$ns connect $tcp2 $sink


set ftp2 [new Application/FTP]
$ftp2 attach-agent $tcp2
$ftp2 set type_ FTP




set null0 [new Agent/Null]
$ns attach-agent $n5 $null0

$ns connect $udp0 $null0  

proc attach-expoo-traffic { node sink size burst idle rate } {

 set ns [Simulator instance]


 set source [new Agent/UDP]
 $ns attach-agent $node $source


 set traffic [new Application/Traffic/Exponential]
      

	  $traffic attach-agent $source
 $ns connect $source $sink
 return $traffic
}
proc track {} {
        global mySink mySink1 myFile1 myFile2 

 set ns [Simulator instance]

	set time 0.5

		set temp1 [$mySink set bytes_]
        set temp2 [$mySink1 set bytes_]
	

        set now [$ns now]

        puts $myFile1 "$now [expr $temp1/$time*8/1000000]"
        puts $myFile2 "$now [expr $temp2/$time*8/1000000]"

        $mySink set bytes_ 0
        $mySink1 set bytes_ 0

        $ns at [expr $now+$time] "track"
}

set mySink [new Agent/LossMonitor]
set mySink1 [new Agent/LossMonitor]
$ns attach-agent $n5 $mySink
$ns attach-agent $n4 $mySink1
set source0 [attach-expoo-traffic $n0 $mySink 200 2s 1s 100k]
set source1 [attach-expoo-traffic $n1 $mySink1 200 2s 1s 200k]

$ns at 0.0 "track"
$ns at 0.5 "$ftp0 start"
$ns at 0.5 "$source0 start"
$ns at 1.0 "$cbr0 start"
$ns at 1.0 "$ftp1 start"
$ns at 1.5 "$ftp2 start"
$ns at 2.0 "$source1 start"
$ns at 4.0 "$ftp0 stop"
$ns at 4.0 "$ftp1 stop"
$ns at 4.0 "$ftp2 stop"
$ns at 4.5 "$cbr0 stop"

$ns at 5.0 "finish"


$ns run
