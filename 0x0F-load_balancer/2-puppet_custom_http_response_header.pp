# Puppet manifest to configure custom HTTP header response

# Define a class for custom HTTP header configuration
class custom_http_header {
    # Package installation
    package { 'nginx':
        ensure => installed,
    }

    # Nginx site configuration
    file { '/etc/nginx/sites-available/default':
        ensure  => file,
        content => "
            server {
                listen 80 default_server;
                listen [::]:80 default_server;

                root /var/www/html;
                index index.html;

                server_name _;

                location / {
                    echo 'Hello World!';

                    # Custom header configuration
                    add_header X-Served-By $hostname;

                    # Other server configurations if needed
                }
            }
        ",
        notify  => Service['nginx'],
    }

    # Symbolic link to enable the site
    file { '/etc/nginx/sites-enabled/default':
        ensure => link,
        target => '/etc/nginx/sites-available/default',
        notify => Service['nginx'],
    }

    # Nginx service management
    service { 'nginx':
        ensure    => running,
        enable    => true,
        hasrestart => true,
    }
}

# Include the custom_http_header class to apply the configuration
include custom_http_header
