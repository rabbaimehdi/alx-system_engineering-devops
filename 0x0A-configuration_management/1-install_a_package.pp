# install flask from pip3 with Puppet
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
