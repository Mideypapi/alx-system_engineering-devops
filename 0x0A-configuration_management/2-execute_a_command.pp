# Manifest to kill a process named killmenow using Puppet
exec { 'killmenow':
  command => 'pkill -f killmenow',
  path    => '/bin:/usr/bin:/sbin:/usr/sbin',
  onlyif  => 'pgrep -f killmenow',
}
