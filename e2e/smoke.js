const http = require('http');
http.get('http://frontend:3000', (res) => {
  if (res.statusCode !== 200) process.exit(1);
  console.log('ok');
});
