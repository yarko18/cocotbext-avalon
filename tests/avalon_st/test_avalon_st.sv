// Copyright 2026 Yaroslav Mariukha
// SPDX-License-Identifier: Apache-2.0

module test_avalon_st #( parameter
    BITS_PER_SYMBOL,
    SYMBOLS_PER_BEAT
) (
    input   clk,
    input   reset,

    output                                          din_ready,
    input                                           din_valid,
    input                                           din_startofpacket,
    input                                           din_endofpacket,
    input [BITS_PER_SYMBOL*SYMBOLS_PER_BEAT-1:0]    din_data,

    input                                           dout_ready,
    output                                          dout_valid,
    output                                          dout_startofpacket,
    output                                          dout_endofpacket,
    output [BITS_PER_SYMBOL*SYMBOLS_PER_BEAT-1:0]   dout_data
);

assign din_ready            = dout_ready;
assign dout_valid           = din_valid;
assign dout_startofpacket   = din_startofpacket;
assign dout_endofpacket     = din_endofpacket;
assign dout_data            = din_data;

    
endmodule