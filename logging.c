/*
 * logging.c
 *
 * Logging functions for pam_afs_session.
 *
 * Logs errors and debugging messages from pam_afs_session functions.  The
 * debug versions only log anything if debugging was enabled; the error
 * versions always log.
 */

#include "config.h"

#ifdef HAVE_SECURITY_PAM_APPL_H
# include <security/pam_appl.h>
# include <security/pam_modules.h>
#elif HAVE_PAM_PAM_APPL_H
# include <pam/pam_appl.h>
# include <pam/pam_modules.h>
#endif
#include <stdarg.h>
#include <stdio.h>
#include <syslog.h>

#include "internal.h"

/*
 * Basic error logging.  Log a message with LOG_ERR priority.
 */
void
pamafs_error(const char *fmt, ...)
{
    char msg[256];
    va_list args;

    va_start(args, fmt);
    vsnprintf(msg, sizeof(msg), fmt, args);
    va_end(args);
    syslog(LOG_ERR, "(pam_afs_session): %s", msg);
}


/*
 * Log a generic debugging message only if debug is enabled.
 */
void
pamafs_debug(struct pam_args *pargs, const char *fmt, ...)
{
    char msg[256];
    va_list args;

    if (!pargs->debug)
        return;

    va_start(args, fmt);
    vsnprintf(msg, sizeof(msg), fmt, args);
    va_end(args);
    syslog(LOG_DEBUG, "(pam_afs_session): %s", msg);
}
