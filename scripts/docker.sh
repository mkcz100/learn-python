DIR="$(cd "$(dirname "$0")" && pwd)"
cd $DIR/../docker/dev
docker-compose up --build