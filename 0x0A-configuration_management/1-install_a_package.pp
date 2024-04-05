# Ensure python3 and pip3 are installed
package { 'python3':
  ensure => installed,
}

package { 'python3-pip':
  ensure => installed,
}

# Upgrade Flask to version 2.1.0 using pip3
exec { 'upgrade_flask':
  command => '/usr/bin/pip3 install --upgrade Flask==2.1.0',
  path    => ['/usr/bin', '/usr/local/bin'],  # Include the path to pip3 and Flask
  require => Package['python3-pip'],          # Ensure python3-pip is installed first
}

# Check for missing dependencies and perform any necessary installations
# Add additional exec resources as needed based on the ImportError message
# For example, if the ImportError mentions missing werkzeug.urls:
exec { 'install_werkzeug':
  command => '/usr/bin/pip3 install --upgrade Werkzeug',
  path    => ['/usr/bin', '/usr/local/bin'],  # Include the path to pip3 and Werkzeug
  require => Exec['upgrade_flask'],            # Ensure Flask upgrade is completed first
}

# Add more exec resources as needed for other dependencies or checks
# ...

# Notify a service or script to restart if Flask or dependencies are upgraded
# For example, if Flask is used with a web server like Nginx or Apache:
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => Exec['upgrade_flask'],  # Restart Nginx after Flask upgrade
}
