# creates a file via puppet

file { '/tmp/holberton/0-create_a_file.pp':
  ensure  => 'file',
  path    => '/etc/holberton',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet'
}