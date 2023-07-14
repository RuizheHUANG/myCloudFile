param(
	[string]$param1
)

if($param1 -eq "clean"){
	python ququ.py clean
}
elseif($param1 -eq "generate"){
	python ququ.py generate
}
elseif($param1 -eq "build"){
	python ququ.py build
}
else{
	Write-Host "请输入clean, generate 或 build"
}