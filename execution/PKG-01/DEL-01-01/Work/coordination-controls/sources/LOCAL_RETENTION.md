# Local capture handling after repository scan

The repository scan flagged a `key selected:` example in the Motwani paper's
extracted text and a token-shaped string in unrelated Bing search markup.
Neither was used as a credential or validated against a service.

The full paper PDF remains unchanged. Its derived `collusion.txt` view replaces
one example-key line with an explicit omission marker; the byte-identical original
is retained at `/Users/ryan/working/hackathons/apart-Nov-26-local-evidence/formation-20261106T212336Z/collusion-original.txt`.
The unrelated search HTML is retained at that directory's `jones-bing.html`, and
its acquisition manifest points to the actual path with the original content hash.
No primary research conclusion relies on that search response. The repository
scanner rules were not changed; neither original is a publication asset.

Original extracted-text SHA-256: `3c9a39b7ae34df9860a255b64836ea0ad0bbd2cf95aa9939ade6fba54ea146c5`.
Repository derived-view SHA-256: `17e7e809f1aa813fcc5518df06d2d06e08d293a8893311acb6ec3af04e01d41b`.
