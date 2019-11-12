set ns [new Simulator]

$ns color 1 Blue
$ns color 2 Red
$ns color 3 Yellow

set nf [open out.nam w]
$ns namtrace-all $nf

set str3 [open trace.tr w]
$ns trace-all $str3

proc finish {} {
	global ns nf
	$ns flush-trace
	close $nf
	exec nam out.nam &
	exit 0
}

set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]
set n4 [$ns node]
set n5 [$ns node]

$ns duplex-link $n0 $n3 2Mb 10ms DropTail
$ns duplex-link $n1 $n3 1.7Mb 25ms DropTail
$ns duplex-link $n2 $n3 3Mb 7ms DropTail
$ns duplex-link $n4 $n3 2.5Mb 9ms DropTail
$ns duplex-link $n5 $n3 2Mb 10ms DropTail

$ns queue-limit $n3 $n1 10
$ns queue-limit $n3 $n5 15

$ns duplex-link-op $n0 $n3 orient left-up
$ns duplex-link-op $n1 $n3 orient up
$ns duplex-link-op $n2 $n3 orient right-up
$ns duplex-link-op $n4 $n3 orient left-down
$ns duplex-link-op $n5 $n3 orient right-down

$ns duplex-link-op $n3 $n5 queuePos 0.5
$ns duplex-link-op $n3 $n1 queuePos 0.6

set tcp1 [new Agent/TCP]
$tcp1 set class_ 2
$ns attach-agent $n0 $tcp1
set sink [new Agent/TCPSink]
$ns attach-agent $n5 $sink
$ns connect $tcp1 $sink
$tcp1 set fid_ 1

set tcp [new Agent/TCP]
$tcp set class_ 2
$ns attach-agent $n4 $tcp
set sink [new Agent/TCPSink]
$ns attach-agent $n1 $sink
$ns connect $tcp $sink
$tcp set fid_ 2

set ftp [new Application/FTP]
$ftp attach-agent $tcp
$ftp set type_ FTP

set ftp1 [new Application/FTP]
$ftp1 attach-agent $tcp1
$ftp1 set type_ FTP

set udp [new Agent/UDP]
$ns attach-agent $n2 $udp
set null [new Agent/Null]
$ns attach-agent $n5 $null
$ns connect $udp $null
$udp set fid_ 3

set cbr [new Application/Traffic/CBR]
$cbr attach-agent $udp
$cbr set type_ CBR
$cbr set packet_size_ 1000
$cbr set rate_ 1mb
$cbr set random_ false

$ns at 0.1 "$cbr start"
$ns at 0.9 "$ftp start"
$ns at 1.2 "$ftp1 start"
$ns at 4.0 "$ftp stop"
$ns at 4.3 "$ftp1 stop"
$ns at 4.5 "$cbr stop"

$ns at 5.0 "finish"

puts "CBR packet size = [$cbr set packet_size_]"
puts "CBR interval = [$cbr set interval_]"

$ns run
