export tag=ericgoebelbecker/difference:latest
docker build . -t $tag
docker push $tag
