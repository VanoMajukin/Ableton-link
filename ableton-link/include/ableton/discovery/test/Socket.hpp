/* Copyright 2016, Ableton AG, Berlin. All rights reserved.
 *
 *  This program is free software: you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation, either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 *  If you would like to incorporate Link into a proprietary software application,
 *  please contact <link-devs@ableton.com>.
 */

#pragma once

#include <ableton/discovery/AsioTypes.hpp>
#include <ableton/util/Log.hpp>
#include <ableton/util/test/IoService.hpp>

namespace ableton
{
namespace discovery
{
namespace test
{

class Socket
{
public:
  Socket(util::test::IoService&)
  {
  }

  friend void configureUnicastSocket(Socket&, const IpAddressV4&)
  {
  }

  std::size_t send(
    const uint8_t* const pData, const size_t numBytes, const discovery::UdpEndpoint& to)
  {
    sentMessages.push_back(
      std::make_pair(std::vector<uint8_t>{pData, pData + numBytes}, to));
    return numBytes;
  }

  template <typename Handler>
  void receive(Handler handler)
  {
    mCallback = [handler](const UdpEndpoint& from, const std::vector<uint8_t>& buffer) {
      handler(from, begin(buffer), end(buffer));
    };
  }

  template <typename It>
  void incomingMessage(const UdpEndpoint& from, It messageBegin, It messageEnd)
  {
    std::vector<uint8_t> buffer{messageBegin, messageEnd};
    mCallback(from, buffer);
  }

  UdpEndpoint endpoint() const
  {
    return UdpEndpoint({}, 0);
  }

  using SentMessage = std::pair<std::vector<uint8_t>, UdpEndpoint>;
  std::vector<SentMessage> sentMessages;

private:
  using ReceiveCallback =
    std::function<void(const UdpEndpoint&, const std::vector<uint8_t>&)>;
  ReceiveCallback mCallback;
};

} // namespace test
} // namespace discovery
} // namespace ableton
