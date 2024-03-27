# Puppet manifest to install and configure Nginx with a 301 redirect

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Define Nginx configuration file
file { '/etc/nginx/sites-available/redirect':
  ensure  => present,
  content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name _;

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    location / {
        root /usr/share/nginx/html;
        index index.html;

        # Custom 404 page
        error_page 404 /404.html;
        location = /404.html {
            root /usr/share/nginx/html;
            internal;
        }

        # Return Hello World on root request
        return 200 'Hello World!\n';
    }

    # Other server configurations if needed
}
",
}

# Create symbolic link for Nginx configuration
file { '/etc/nginx/sites-enabled/redirect':
  ensure => link,
  target => '/etc/nginx/sites-available/redirect',
}

# Remove default Nginx configuration
file { '/etc/nginx/sites-enabled/default':
  ensure => absent,
}

# Restart Nginx to apply changes
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/redirect'],
}

