# aria2-dl
youtube-dl + aria2

## Requirement: 

- Python 3
- youtube-dl >= 2017.10.0


## Usage: 

Run aria2c with rpc enabled

``` aria2c --enable-rpc --rpc-listen-all=true --rpc-allow-origin-all ```

Add URL to aria2c via RPC

```./addurl.py http://localhost:6800/rpc http://video.url ```
