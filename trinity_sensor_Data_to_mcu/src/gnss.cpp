#include "gnss.hpp"

uint8_t gnss_get_message(char *str_buf, const char *keyword)
{
    char line_buf[GNSS_SENTENCE_BUFFER_SIZE];
    uint8_t line_idx = 0;

    uint16_t read_attempts = GNSS_SENTENCE_READ_ATTEMPTS;
    for (uint8_t ch = GnssSerial.read(); ch != '\n';)
    {
        if (GnssSerial.available())
        {
            if (ch >= 32 && ch <= 126)
            {
                if (ch == '$')
                {
                    memset(line_buf, 0, sizeof(line_buf));
                    line_idx = 0;
                }
                line_buf[line_idx] = ch;
                line_idx++;
            }
            ch = GnssSerial.read();
        }
        else
        {
            read_attempts--;
        }
        if (!read_attempts)
        {
            return 0;
        }
    }

    line_buf[line_idx] = '\0';
    GnssSerial.flush();

    if (strstr(line_buf, keyword))
    {
        if (gnss_is_msg_valid(line_buf))
        {
            strncpy(str_buf, line_buf, line_idx);
            str_buf[line_idx] = '\0';
            return 1;
        }
    }

    return 0;
}

bool gnss_is_msg_valid(char *str_buf)
{
    const char *start = strchr(str_buf, '$');
    const char *end = strchr(start, '*');

    if (start && end)
    {
        uint8_t checksum = 0;
        for (const char *ch = start + 1; ch < end; ch++)
        {
            checksum ^= *ch;
        }

        uint8_t messageChecksum = 0;
        uint8_t checksumChar_1 = *(end + 1);
        if (checksumChar_1 >= '0' && checksumChar_1 <= '9')
        {
            messageChecksum += (checksumChar_1 - '0') << 4;
        }
        else if (checksumChar_1 >= 'A' && checksumChar_1 <= 'F')
        {
            messageChecksum += (10 + checksumChar_1 - 'A') << 4;
        }
        else if (checksumChar_1 >= 'a' && checksumChar_1 <= 'f')
        {
            messageChecksum += (10 + checksumChar_1 - 'a') << 4;
        }

        uint8_t checksumChar_2 = *(end + 2);
        if (checksumChar_2 >= '0' && checksumChar_2 <= '9')
        {
            messageChecksum += (checksumChar_2 - '0');
        }
        else if (checksumChar_2 >= 'A' && checksumChar_2 <= 'F')
        {
            messageChecksum += (10 + checksumChar_2 - 'A');
        }
        else if (checksumChar_2 >= 'a' && checksumChar_2 <= 'f')
        {
            messageChecksum += (10 + checksumChar_2 - 'a');
        }

        return checksum == messageChecksum;
    }

    return false;
}
