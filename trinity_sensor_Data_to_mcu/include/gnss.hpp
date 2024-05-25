#ifndef GNSS_HPP
#define GNSS_HPP

#include <stdint.h>

#include "init.hpp"

#define GNSS_SENTENCE_BUFFER_SIZE 128
#define GNSS_SENTENCE_READ_ATTEMPTS UINT16_MAX

uint8_t gnss_get_message(char *str_buf, const char *keyword);
bool gnss_is_msg_valid(char *str_buf);

#endif
