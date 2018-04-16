
#
# Block required for Zigbee Scanning
# Copyright (C) 2018 Team SUPERFREQ, CU Boulder ITP <itp@colorado.edu>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#


import numpy as np
from gnuradio import gr
import pmt

class blk(gr.basic_block):
    """Convert Zigbee Link Quality Indicator (LQI) (0..255) 
       to RFtap signal quality field (qual) (0.0..1.0)"""

    def __init__(self):
        gr.basic_block.__init__(
            self,
            name='LQI to qual',   # will show up in GRC
            in_sig=[],
            out_sig=[]
        )
        self.message_port_register_in(pmt.intern('in'))
        self.set_msg_handler(pmt.intern('in'), self.handle_msg)
        self.message_port_register_out(pmt.intern('out'))

    def handle_msg(self, pdu):
        meta, data = pmt.to_python(pdu)
        meta['qual'] = meta['lqi'] / 255.0
        pduout = pmt.cons(pmt.to_pmt(meta), pmt.to_pmt(data))
        self.message_port_pub(pmt.intern('out'), pduout)

