# installs puppet-lint via puppet

package { 'puppet-lint':
  ensure   => '2.1.1',
  name     => 'puppet-lint',
  provider => 'gem',
}