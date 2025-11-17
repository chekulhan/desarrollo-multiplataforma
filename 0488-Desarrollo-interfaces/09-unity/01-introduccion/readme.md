docker build -t unity-dev .

In Powershell:
docker run -it -v ${PWD}:/app --name unity unity-dev


In /programs, crear una plantilla by running 
dotnet new console

Y compilar y ejecutar:
dotnet run -c Release
