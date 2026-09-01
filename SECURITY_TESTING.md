# Authorized security-testing fixture

This repository's current branches are intentionally disarmed. The collector is
set to `.invalid`, the transport fails closed while that placeholder is present,
and the README uses the neutral control profile.

The exact authorized test revisions are pinned as
`spk004-r10-control-tested` and `spk004-r10-trigger-tested`. Reproduction must
use only a disposable account and a private, triager-controlled HTTPS receiver.
Never place a production credential in the receiver. Clear its request buffer
and revoke or retire the disposable account immediately after testing.
