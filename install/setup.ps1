# generated from colcon_powershell/shell/template/prefix_chain.ps1.em

# This script extends the environment with the environment of other prefix
# paths which were sourced when this file was generated as well as all packages
# contained in this prefix path.

# function to source another script with conditional trace output
# first argument: the path of the script
function _colcon_prefix_chain_powershell_source_script {
  param (
    $_colcon_prefix_chain_powershell_source_script_param
  )
  # source script with conditional trace output
  if (Test-Path $_colcon_prefix_chain_powershell_source_script_param) {
    if ($env:COLCON_TRACE) {
      echo ". '$_colcon_prefix_chain_powershell_source_script_param'"
    }
    . "$_colcon_prefix_chain_powershell_source_script_param"
  } else {
    Write-Error "not found: '$_colcon_prefix_chain_powershell_source_script_param'"
  }
}

# source chained prefixes
_colcon_prefix_chain_powershell_source_script "/home/aakash/summer_camp_ws/devel\local_setup.ps1"
_colcon_prefix_chain_powershell_source_script "/home/aakash/catkin_ws/devel\local_setup.ps1"
_colcon_prefix_chain_powershell_source_script "/opt/ros/humble\local_setup.ps1"
_colcon_prefix_chain_powershell_source_script "/home/aakash/practice_ws/install\local_setup.ps1"
_colcon_prefix_chain_powershell_source_script "/home/aakash/ros2practice/install\local_setup.ps1"
_colcon_prefix_chain_powershell_source_script "/home/aakash/turtlebot3_ws/install\local_setup.ps1"
_colcon_prefix_chain_powershell_source_script "/home/aakash/neobotix_workspace/install\local_setup.ps1"
_colcon_prefix_chain_powershell_source_script "/home/aakash/simulation2_ws/install\local_setup.ps1"
_colcon_prefix_chain_powershell_source_script "/home/aakash/intelligent_quads/ardu_ws/install\local_setup.ps1"
_colcon_prefix_chain_powershell_source_script "/home/aakash/ros2_ws/install\local_setup.ps1"
_colcon_prefix_chain_powershell_source_script "/home/aakash/flytbase/ros2_ws/install\local_setup.ps1"
_colcon_prefix_chain_powershell_source_script "/home/aakash/flytbase/ros_ws/install\local_setup.ps1"
_colcon_prefix_chain_powershell_source_script "/home/aakash/flytbase_ws/install\local_setup.ps1"
_colcon_prefix_chain_powershell_source_script "/home/aakash/eyantra_ws/install\local_setup.ps1"

# source this prefix
$env:COLCON_CURRENT_PREFIX=(Split-Path $PSCommandPath -Parent)
_colcon_prefix_chain_powershell_source_script "$env:COLCON_CURRENT_PREFIX\local_setup.ps1"
