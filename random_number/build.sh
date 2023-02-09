export tag=ericgoebelbecker/random_number:latest
docker build . -t $tag
docker push $tag
