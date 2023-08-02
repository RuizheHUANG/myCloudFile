param (
    [string]$param1,
    [string]$platform
)

if ($param1 -eq "clean") {
    python ququ.py clean
}
elseif ($param1 -eq "generate") {
    python ququ.py generate
}
elseif ($param1 -eq "build") {
    python ququ.py build
}
elseif ($param1 -eq "package") {
    if ($PSBoundParameters.ContainsKey('platform')) {
	$platform = $platform.Split('=')[1]
        if ($platform -eq "windows") {
            python ququ.py package-Win64
        }
        elseif ($platform -eq "android") {
            python ququ.py package-Android
        }
        elseif ($platform -eq "ios") {
            python ququ.py package-IOS
        }
        else {
            Write-Host "Invalid platform argument: $platform"
        }
    }
    else {
        Write-Host 'Missing platform argument. Please use "--platform=windows", "--platform=android", or "--platform=ios"'
    }
}
else {
    Write-Host 'Unknown command, please enter "clean", "generate", "build", or "package"'
}
