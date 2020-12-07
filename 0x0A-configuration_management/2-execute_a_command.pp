# installs puppet-lint via puppet

exec { 'killmenow':
  command  => 'pkill -f killmenow',
  path     => 'usr/bin/',
  provider => 'bash'
}