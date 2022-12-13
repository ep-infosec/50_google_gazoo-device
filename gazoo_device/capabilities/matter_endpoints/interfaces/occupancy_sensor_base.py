# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Interface for a Matter Occupancy Sensor endpoint."""
import abc
from gazoo_device.capabilities.matter_clusters.interfaces import occupancy_sensing_base
from gazoo_device.capabilities.matter_endpoints.interfaces import endpoint_base


class OccupancySensorBase(endpoint_base.EndpointBase, metaclass=abc.ABCMeta):
  """Matter Occupancy Sensor endpoint interface."""

  DEVICE_TYPE_ID = 0x0107

  @property
  @abc.abstractmethod
  def occupancy_sensing(
      self) -> occupancy_sensing_base.OccupancySensingClusterBase:
    """Required cluster: occupancy_sensing cluster."""