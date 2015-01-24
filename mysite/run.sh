echo "stop server..."
id=`ps -ef|grep python|grep 8000| awk -F ' ' '{print $2}'`
echo $id
if [ -n "$id" ];
then
   cmd=`kill -9 $id`
   $cmd
   echo "kill $id"
else
   echo "server not running..."
fi

echo "start server..."
nohup python ../manage.py runserver 0.0.0.0:8000 > site.log &
echo "server running"
