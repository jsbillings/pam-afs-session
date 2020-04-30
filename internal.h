/*
 * Internal prototypes and structures for pam-afs-session.
 *
 * Written by Russ Allbery <eagle@eyrie.org>
 * Copyright 2006, 2007, 2008, 2010, 2011
 *     The Board of Trustees of the Leland Stanford Junior University
 *
 * See LICENSE for licensing terms.
 */

#ifndef INTERNAL_H
#define INTERNAL_H 1

#include <config.h>
#ifdef HAVE_KERBEROS
# include <portable/krb5.h>
#endif
#include <portable/pam.h>
#include <portable/macros.h>
#include <portable/stdbool.h>

#include <stdarg.h>

/* Forward declarations to avoid unnecessary includes. */
struct pam_args;
struct passwd;
struct vector;

/* Used for unused parameters to silence gcc warnings. */
#define UNUSED  __attribute__((__unused__))

/*
 * The global structure holding our arguments from the PAM configuration.
 * Filled in by pamafs_init.
 */
struct pam_config {
    struct vector *afs_cells;   /* List of AFS cells to get tokens for. */
    bool aklog_homedir;         /* Pass -p <homedir> to aklog. */
    bool always_aklog;          /* Always run aklog even w/o KRB5CCNAME. */
    bool debug;                 /* Log debugging information. */
    bool ignore_root;           /* Skip authentication for root. */
    bool kdestroy;              /* Destroy ticket cache after aklog. */
    long minimum_uid;           /* Ignore users below this UID. */
    bool nopag;                 /* Don't create a new PAG. */
    bool notokens;              /* Only create a PAG, don't obtain tokens. */
    bool no_afs_check;          /* Don't attempt to probe for AFS */
    struct vector *program;     /* Program to run for tokens. */
    bool retain_after_close;    /* Don't destroy the cache on session end. */
};

BEGIN_DECLS

/* Default to a hidden visibility for all internal functions. */
#pragma GCC visibility push(hidden)

/* Parse the PAM flags and arguments and fill out pam_args. */
struct pam_args *pamafs_init(pam_handle_t *, int flags, int argc,
                             const char **argv);

/* Free the pam_args struct when we're done. */
void pamafs_free(struct pam_args *);

/* Token manipulation functions. */
int pamafs_token_get(struct pam_args *, bool reinitialize);
int pamafs_token_delete(struct pam_args *);

/* Undo default visibility change. */
#pragma GCC visibility pop

END_DECLS

#endif /* INTERNAL_H */
